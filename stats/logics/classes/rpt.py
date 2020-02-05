"""Clases referentes a el manejo y proceso de archivos RPT"""

from datetime import timedelta, datetime
import re
from collections import defaultdict
from enum import Enum

try:
    from stats.logics.classes.errors import NoHayArchivo, NoHayFecha, NoHayRegistroAsistencia
except ImportError:
    from errors import NoHayArchivo, NoHayFecha, NoHayRegistroAsistencia

class Cons(Enum):
    """Clase que define los textos constantes usados en la app"""

    FORMATO_HORA = "%H:%M:%S"
    FORMATO_FECHA = "%Y/%m/%d"

    TARDE = "Tarde"
    ASISTE = "Asiste"
    FALTA = "Falta"

    CONECTADO = "conectado"
    DESCONECTADO = "desconectado"

    NOMBRE_MISION = "NOMBRE_MISION"
    DESC_MISION = "DESC_MISION"
    AUTOR_MISION = "AUTOR_MISION"
    TIPO_MISION = "TIPO_MISION"
    NOMBRE_CAMPA = "NOMBRE_CAMPA"
    ES_OFICIAL = "ES_OFICIAL"
    MAPA_MISION = "MAPA_MISION"


class RPT():
    fecha = None
    data_raw = None
    data_mision = None
    data_asistencia = []
    data_mision = []
    data_estadistica = []

    sesiones_asistencia = dict()
    

    ajuste = "+1" #FIXME actual ajuste de horario de servidor a Venezuela. Si cambia servidor o huso horario, modificar!

    data_final = {
        "mision":"",
        "autor":"",
        "desc":"",
        "mapa":"",
        "oficial":False,
        "tipo":"",
        "nombre_campa":"",
        "fecha": "",
        "asistencias":[],
        "eventos":[]
    }


    def __init__(self, archivo=None):
        self.archivo = archivo
        
        if archivo is None:
            raise NoHayArchivo()

        self.data_raw = self.abrir_archivo(archivo)
        self.sesiones_asistencia = dict()

        self.leer_rpt_asistencia()
        self.leer_rpt_mision()

    def abrir_archivo(self, archivo):
        """Abre un archivo y devuelve su contenido"""
        archivo = open(archivo, 'r', encoding='UTF-8')
        data = archivo.read()
        archivo.close()

        return data


    def leer_rpt_asistencia(self):
        """Lee el RPT y extrae los eventos necesarios para calcular asistencia.

        Retorna diccionario en formato: {jugador: [fecha, hora, evento]}"""

        self.sesiones_asistencia = list()

        # Busca en el rpt todas las referencias a ZRASISTENCIA
        busqueda = re.findall('^.*"ZRASISTENCIA.*$', self.data_raw, re.M)
        asistencias = list()
        if not busqueda:
            raise NoHayRegistroAsistencia(self.archivo)

        for asistencia in busqueda:
            asistencia = asistencia.split(" ") # ejemplo [2020/01/21,19:37:54,"ZRASISTENCIA:,SgtM.Tano,conectado]
            asistencia.pop(2) #elimina elemento "ZRASISTENCIA" de la lista

            fecha = asistencia[0].strip(",")
            hora = asistencia[1]
            jugador = asistencia[2]
            evento = (asistencia[3])

            asistencia[0] = fecha
            asistencia[1] = self.ajuste_horario(hora, self.ajuste)

            asistencias.append(asistencia)

            self.sesiones_asistencia = defaultdict(list)
            for evento in asistencias:
                jugador = evento[2]
                self.sesiones_asistencia[jugador].append([evento[0], evento[1], (evento[3]).replace('"', "")])

                if evento == asistencias[-1]:
                    self.fecha = fecha

            #Eliminando eventos del jugador __SERVER__
            self.sesiones_asistencia.pop("__SERVER__", None)

        for jugador, eventos in self.sesiones_asistencia.items():
            asistencia = Asistencia(jugador, eventos)
            self.data_asistencia.append(asistencia.dicc())

        self.data_final["asistencias"] = self.data_asistencia

    def leer_rpt_mision(self):
        # Busca en el rpt todas las referencias a ZRASISTENCIA
        busqueda = re.findall('^.*"ZRSTATS.*$', self.data_raw, re.M)

        datos_mision = DatoMision(busqueda)
        self.data_final["mision"] = datos_mision.mision
        self.data_final["autor"] = datos_mision.autor
        self.data_final["desc"] = datos_mision.desc
        self.data_final["mapa"] = datos_mision.mapa
        self.data_final["oficial"] = datos_mision.oficial
        self.data_final["tipo"] = datos_mision.tipo
        self.data_final["nombre_campa"] = datos_mision.nombre_campa
        self.data_final["fecha"] = self.fecha

    def ajuste_horario(self, hora, ajuste:str):
        """Ajusta la hora del reporte para coincidir con la hora de Venezuela.
        Params:
            hora   -- hora del evento a corregir en formato h:m:s
            ajuste -- expresión que se usará para evaluar la diferencia horaria,
                      por ejemplo: +4 sumaría 4 horas a la hora original.

        Retorna la hora de Venezuela."""

        ###### Actual diferencia horaria del servidor es +1 ##########

        h = int((hora.split(":"))[0])
        m = (hora.split(":"))[1]
        s = (hora.split(":"))[2]

        hora_venez = eval(f"{h}{ajuste}")
        if hora_venez >= 24:
            hora_venez = abs(24 - hora_venez)

        hora_venez = f"{hora_venez}:{m}:{s}"

        return hora_venez

class Asistencia():
    """Clase que manipula y procesa la información parseada desde el RPT y
    genera el diccionario con información de asistencia
    :params
        jugador:str -- Nombre del jugador en formato rango.nombre
        eventos:list -- Lista de listas con cada evento de conexión y desconexión
    """

    hora_ingreso = timedelta(hours=21, minutes=0, seconds=0)
    hora_fin = timedelta(hours=23, minutes=0, seconds=0)
    hora_ingreso_limite = timedelta(hours=21, minutes=15, seconds=0)
    tiempo_total_asistencia_valida = timedelta(hours=1, minutes=20, seconds=0)
    tiempo_minimo_problema = timedelta(minutes=30)
    
    asistencia = Cons.FALTA.value
    requiere_atencion = False
    atrasado = False

    jugador = str()
    eventos = list()

    sesion_total = timedelta(hours=0, minutes=0, seconds=0)

    def __init__(self, jugador:str, eventos:list):
        self.jugador = jugador
        self.eventos = eventos

        self.definir_atraso()
        self.contar_tiempo_total_sesion()
        self.validar_sesion()
        self.dicc()

    def definir_atraso(self):
        t = datetime.strptime(self.eventos[0][1], "%H:%M:%S")
        ingreso_jugador = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
        if ingreso_jugador > self.hora_ingreso:
            self.asistencia = Cons.TARDE.value

    def contar_tiempo_total_sesion(self):
        for evento in self.eventos:
            if evento[-1] == Cons.CONECTADO.value:
                fecha_conectado = evento[0]
                d = datetime.strptime(fecha_conectado, Cons.FORMATO_FECHA.value)
                hora_conectado = evento[1]
                t = datetime.strptime(hora_conectado, Cons.FORMATO_HORA.value)

                conexion = datetime(d.year, d.month, d.day, t.hour, t.minute, t.second)
 
                try:
                    fecha_desconectado = self.eventos[self.eventos.index(evento)+1][0]
                    d = datetime.strptime(fecha_desconectado, Cons.FORMATO_FECHA.value)
                    hora_desconectado = self.eventos[self.eventos.index(evento)+1][1]
                    t = datetime.strptime(hora_desconectado, Cons.FORMATO_HORA.value)

                    desconexion = datetime(d.year, d.month, d.day, t.hour, t.minute, t.second)
                except IndexError:
                    print(f"{self.jugador} no tiene un evento de desconexión!")
                    print(f"asumiendo {self.hora_fin} como horario de desconexión!")
                    conexion = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
                    desconexion = self.hora_fin
                    self.sesion_total = abs(desconexion - conexion)

                    return 
                else:
                    duracion_conexion = abs(desconexion - conexion)
                    self.sesion_total = self.sesion_total + duracion_conexion

    def  validar_sesion(self):
        if self.sesion_total > self.tiempo_total_asistencia_valida:
            self.asistencia = Cons.ASISTE.value

            if self.atrasado:
                self.asistencia = Cons.TARDE.value

        elif self.sesion_total <= self.tiempo_total_asistencia_valida and self.sesion_total > self.tiempo_minimo_problema:
            self.requiere_atencion = True
        else:
            self.asistencia = Cons.FALTA.value
            self.requiere_atencion = True

    def dicc(self):
        try:
            nombre = self.jugador.split(".")
            rango = nombre[0]
            nombre = nombre[1]
        except IndexError:
            print("Algún pastelito olvidó ponerse el rango")
            print(f"{self.jugador}")
            nombre = self.jugador

        diccionario_jugador = {
            "nombre":nombre,
            "rango":rango,
            "asistencia":self.asistencia,
            "tiempo_sesion":str(self.sesion_total),
            "requiere_atencion":str(self.requiere_atencion)
        }

        return diccionario_jugador

class DatoMision():
    """Clase que manipula y procesa la información parseada desde el RPT y
    devuelve datos de misión.
    :params
        busqueda:list -- lista con el resultado de buscar ZRSTATS
    """
    mision = str()
    autor = str()
    desc = str()
    mapa = None
    oficial = False
    tipo = "OTRO"
    nombre_campa = None
    busqueda = list()

    def __init__(self, busqueda:list):
        self.busqueda = busqueda

        self.parsear_claves()

    def parsear_claves(self):
        for linea in self.busqueda:
            linea = linea.split(" ")
            clave = linea[3]
            valor = linea[4:]
            valor = " ".join(valor)
            valor = valor.strip('"')

            if clave == Cons.NOMBRE_MISION.value:
                self.mision = valor
            elif clave == Cons.AUTOR_MISION.value:
                self.autor = valor
            elif clave == Cons.DESC_MISION.value:
                self.desc = valor
            elif clave == Cons.MAPA_MISION.value:
                self.mapa = valor
            elif clave == Cons.ES_OFICIAL.value:
                self.oficial = bool(valor)
            elif clave == Cons.TIPO_MISION.value:
                self.tipo = valor
            elif clave == Cons.NOMBRE_CAMPA.value:
                self.nombre_campa = valor


if __name__ == "__main__":
    """local test"""
    reporte = RPT("stats/logics/reporte_prueba.rpt")

    from pprint import pprint

    pprint(reporte.data_final)