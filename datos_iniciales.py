"""Agrega los datos iniciales de forma automática"""

from stats.models import *
from collections import defaultdict
import os
import random
import datetime

lista = [Miembro, Rango, Unidad, Rol, Nacionalidad, Clase, User, Asistencia, Mision, Campana]
for item in lista:
    item.objects.all().delete()


def crear_unidades():
    unidades_dict = {
        'altm': ['Alto Mando', 'ALTM'],
        'infm': ['Inf. de Marines', 'IMZR'],
        'paraca': ['Paracaidistas', 'PAR'],
        'echo': ['Espectro', 'ECHO'],
        'cab': ['Caballería', 'CAB'],
        'fazr': ['Fuerza Aérea', 'FAZR'],
    }

    print('Creando Unidades...')

    for var, array in unidades_dict.items():
        var = Unidad.objects.create()
        var.nombre = array[0]
        var.abreviatura = array[1]
        var.save()


def crear_rango():
    rangos_dict = {
        'may': ['Mayor', 'May', 0],
        'cap': ['Capitán', 'Cap', 1],
        'tte': ['Teniente', 'Tte', 2],
        'alf': ['Alférez', 'Alf', 3],
        'sgtm': ['Sargento Mayor', 'SgtM', 4],
        'sgt1': ['Sargento 1º', 'Sgt1', 5],
        'sgt': ['Sargento', 'Sgt', 6],
        'cbo1': ['Cabo 1º', 'Cbo1', 7],
        'cbo': ["Cabo", 'Cbo', 8],
        'dis': ['Distinguido', 'Dis', 9],
        'inf': ['Infante', 'Inf', 10],
        'rct': ['Recluta', 'Rct', 11],
        'asp': ['Aspirante', 'Asp', 12]
    }

    print('Creando rangos...')

    for var, array in rangos_dict.items():
        var = Rango.objects.create()
        var.rango = array[0]
        var.abreviatura = array[1]
        var.orden = array[2]
        var.save()


def crear_rol():
    roles_dict = {
        'nada': ['--', '--'],
        'cmd': ['Comandante Unidad', 'CMD'],
        'ce': ['Comandante Escuadra', 'CE'],
        'lea': ['Líder Equipo A', 'LEA'],
        'leb': ['Líder Equipo B', 'LEB'],
        'a':['ALPHA', 'A'],
        'b':['BRAVO', 'B'],
        'cmda1':['Com. Ariete 1', 'CMDA1'],
        'cmda2':['Com. Ariete 2', 'CMDA2'],
        'cmda3':['Com. Ariete 3', 'CMDA3'],
        'cmda4':['Com. Ariete 4', 'CMDA4']
    }

    print('Creando roles...')

    for var, array in roles_dict.items():
        var = Rol.objects.create()
        var.rol = array[0]
        var.abreviatura = array[1]
        var.save()


def crear_clase():
    clases_dict = {
        'nada': ['--', '--'],
        'fl': ['Fusilero', 'FL'],
        'mg': ['Ametrallador', 'MG'],
        'at': ['Antitanque', 'AT'],
        'gl': ['Granadero', 'GL'],
        'mc': ['Médico de combate', 'MC'],
        'od': ['Operador de dron', 'OD'],
        'ro': ['Radio operador', 'RO'],
        'te': ['Tirador de escuadra', 'TE']
    }

    print('Creando clases...')

    for var, array in clases_dict.items():
        var = Clase.objects.create()
        var.clase = array[0]
        var.abreviatura = array[1]
        var.save()


def crear_naciones():
    # TODO no habrá un template con todos los países como en cualquier formulario web?
    naciones_dict = {
        'arg': ['Argentina', 'ARG'],
        'cl': ['Chile', 'CL'],
        'co': ['Colombia', 'CO'],
        'cr': ['Costa Rica', 'CR'],
        'sv': ['El Salvador', 'SV'],
        'jp': ['Japón', 'JP'],
        'mx': ['México', 'MX'],
        'pa': ['Panamá', 'PA'],
        'py': ['Paraguay', 'PY'],
        'pe': ['Perú', 'PE'],
        'us': ['United States', 'US'],
        've': ['Venezuela', 'VE'],
        'pr': ['Puerto Rico', 'PR'],
        'bo': ['Bolivia', 'BO'],
        'rd': ['República Dominicana', 'RD'],
        'ca': ['Canadá', 'CA']
    }

    print('Creando naciones...')

    for var, array in naciones_dict.items():
        var = Nacionalidad.objects.create()
        var.pais = array[0]
        var.abreviatura = array[1]
        var.save()


def agregar_miembros():
    #rango|nombre|clase1|clase2|nac|est|unidad|pel|esc|rol
    # 0      1      2     3      4   5     6    7   8   9

    script_dir = os.path.dirname(os.path.realpath(__file__))
    datos_iniciales = script_dir + '\\datos_iniciales.txt'
    with open(datos_iniciales) as txt:
        for line in txt.readlines():
            array = line.replace('\n', '').split(' ')
            #print(array)
            user = User.objects.create_user(username=array[1], email=array[1]+"@zrarmy.com", password=array[1].lower())
            miembro = Miembro.objects.get(nombre=array[1])
            miembro.nombre = array[1]
            #print(miembro.nombre)
            miembro.rango = Rango.objects.get(abreviatura = array[0])
            #print(miembro.rango)
            miembro.clase1 = Clase.objects.get(abreviatura = array[2])
            #print(miembro.clase1)
            miembro.clase2 = Clase.objects.get(abreviatura = array[3])
            #print(miembro.clase2)
            miembro.nacionalidad = Nacionalidad.objects.get(abreviatura = array[4])
            #print(miembro.nacionalidad)

            if array[5] == 'A':
                el_estado = 'Activo'
            elif array[5] == 'R':
                el_estado = 'Reserva'
            miembro.estado = el_estado
            #print(miembro.estado)
            miembro.unidad = Unidad.objects.get(abreviatura = array[6])
            #print(miembro.unidad)
            miembro.peloton = array[7]
            #print(miembro.peloton)
            miembro.escuadra = array[8]
            #print(miembro.escuadra)
            miembro.rol = Rol.objects.get(abreviatura = array[9])
            #print(miembro.rol)
            miembro.save()
            #print(miembro)


def crea_mision_ofi(fecha, campana, i, miembros):
    mision = Mision()
    mision.nombre = "Mision " + str(i) + " de " + fecha.strftime("%b")
    mision.fecha_finalizada = fecha
    mision.fecha_creacion = fecha
    mision.tipo = Mision.TIPO_CAMPANA
    mision.estado = Mision.ESTADO_FINALIZADA
    mision.campana = campana
    mision.descripcion = "Campaña jugada durante el mes de " + fecha.strftime("%B")
    mision.save()

    t = datetime.datetime.strptime("02:30:15", '%H:%M:%S')
    delta = datetime.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
    for m in miembros:
        if random.choice([True, False]):
            a = Asistencia.objects.create(mision=mision, miembro=m, fecha=mision.fecha_finalizada,
                                          asistencia=Asistencia.ASIST_ASISTE, tiempo_de_sesion=delta)
        else:
            if random.choice([True, False]):
                a = Asistencia.objects.create(mision=mision, miembro=m, fecha=mision.fecha_finalizada,
                                              asistencia=Asistencia.ASIST_FALTA, tiempo_de_sesion=delta)
            else:
                a = Asistencia.objects.create(mision=mision, miembro=m, fecha=mision.fecha_finalizada,
                                              asistencia=Asistencia.ASIST_TARDE, tiempo_de_sesion=delta)



def crea_mision_asp(fecha, camp_asp, ai, aspirantes):
    mis_asp = Mision()
    mis_asp.nombre = "Aspirantes curso " + str(ai) + " Camada de " + fecha.strftime("%b")
    mis_asp.fecha_finalizada = fecha
    mis_asp.fecha_creacion = fecha
    mis_asp.tipo = Mision.TIPO_CURSO
    mis_asp.estado = Mision.ESTADO_FINALIZADA
    mis_asp.campana = camp_asp
    mis_asp.descripcion = "Dia " + str(ai) + " de la camada Aspirante del mes de " + fecha.strftime("%B")
    mis_asp.save()
    t = datetime.datetime.strptime("02:30:15", '%H:%M:%S')
    delta = datetime.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
    for m in aspirantes:
        if random.choice([True, False]):
            a = Asistencia.objects.create(mision=mis_asp, miembro=m, fecha=mis_asp.fecha_finalizada,
                                          asistencia=Asistencia.ASIST_ASISTE, tiempo_de_sesion=delta)
        else:
            if random.choice([True, False]):
                a = Asistencia.objects.create(mision=mis_asp, miembro=m, fecha=mis_asp.fecha_finalizada,
                                              asistencia=Asistencia.ASIST_FALTA, tiempo_de_sesion=delta)
            else:
                a = Asistencia.objects.create(mision=mis_asp, miembro=m, fecha=mis_asp.fecha_finalizada,
                                              asistencia=Asistencia.ASIST_TARDE, tiempo_de_sesion=delta)


def crea_mision_impro(fecha, miembros):
    mision = Mision()
    mision.nombre = "Impro del dia " + fecha.strftime("%Y / %d / %b")
    mision.fecha_finalizada = fecha
    mision.fecha_creacion = fecha
    mision.tipo = Mision.TIPO_IMPROVISADA
    mision.estado = Mision.ESTADO_FINALIZADA
    mision.descripcion = "Improvisada"
    mision.save()
    t = datetime.datetime.strptime("02:30:15", '%H:%M:%S')
    delta = datetime.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
    for m in miembros:
        if random.choice([True, False]):
            a = Asistencia.objects.create(mision=mision, miembro=m, fecha=mision.fecha_finalizada,
                                          asistencia=Asistencia.ASIST_ASISTE, tiempo_de_sesion=delta)
        else:
            if random.choice([True, False]):
                a = Asistencia.objects.create(mision=mision, miembro=m, fecha=mision.fecha_finalizada,
                                              asistencia=Asistencia.ASIST_FALTA, tiempo_de_sesion=delta)
            else:
                a = Asistencia.objects.create(mision=mision, miembro=m, fecha=mision.fecha_finalizada,
                                              asistencia=Asistencia.ASIST_TARDE, tiempo_de_sesion=delta)


def generar_misiones():
    print("Generado misiones, campañas y asistencias")
    # Genero campañas
    fecha = datetime.date(2019, 1, 1)
    fecha_fin = datetime.date(now().year, now().month, now().day)
    #fecha_fin = datetime.date(2019, 2, 1)
    dia = datetime.timedelta(days=1)
    mes = 0
    miembros = Miembro.objects.exclude(rango__abreviatura='Asp')
    aspirantes = Miembro.objects.filter(rango__abreviatura='Asp')
    while fecha <= fecha_fin:

        if mes < fecha.month:  # cambio de mes y creo campaña
            i = 1  # numero de mision dentro de la campaña
            ai = 1  # numero de curso asp
            mes += 1
            campana = Campana()
            campana.nombre = "Campaña de " + fecha.strftime("%B")
            campana.tipo = Campana.TIPO_CAMPANA
            campana.estado = Campana.ESTADO_FINALIZADA
            campana.save()

            camp_asp = Campana()
            camp_asp.nombre = "Camada Asp. de " + fecha.strftime("%B")
            camp_asp.tipo = Campana.TIPO_CURSO
            camp_asp.estado = Campana.ESTADO_FINALIZADA
            camp_asp.save()

        if fecha.weekday() == 1:  # martes
            crea_mision_ofi(fecha, campana, i, miembros)
            i += 1
            crea_mision_asp(fecha, camp_asp, ai, aspirantes)
            ai += 1
        elif fecha.weekday() == 2:  # miercoles
            crea_mision_asp(fecha, camp_asp, ai, aspirantes)
            ai += 1
        elif fecha.weekday() == 3:  # jueves
            crea_mision_ofi(fecha, campana, i, miembros)
            i += 1
        else:
            if random.choice([True, False]):  # 20% de chance de generar una impro un dia no oficial
                crea_mision_impro(fecha, miembros)

        fecha = fecha + dia  # Avanzo el dia en el calendario
    print("FINALIZADO AGREAGAR MISIONES Y ASISTENCIAS")




def main():
    crear_unidades()
    crear_rango()
    crear_rol()
    crear_clase()
    crear_naciones()
    agregar_miembros()
    generar_misiones()
    # Le pongo permisos al usuario admin
    user = User.objects.get(username="Admin")
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print("FINALIZADO DATOS INICIALES")


if __name__ == '__main__':
    main()
