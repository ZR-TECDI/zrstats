#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
"""Recolecta información desde el archivo RPT para validar o invalidar asistencia y luego pasarlo a una tabla."""
 
# imports
import re
from collections import defaultdict
import datetime
import asistencia.ArmaStats.DATA_to_ZRASISTENCIA as cdata
from django.conf import settings

# global variables
#global data
#data = "data2.rpt"

global conectados
conectados = []

# funciones
def leer_rpt(uploadfile):
    """Lee y ordena el contenido del archivo RPT.

Retorna un diccionario de formato: {jugador: [[fecha, hora, conectado/desconectado]]"""


    data = uploadfile
    rpt_total = []
    with open(settings.BASE_DIR+'\\asistencia\\ArmaStats\\'+data, 'r') as f:
        s = "\n"
        l = s.join((f.readlines()))   
        rpt = re.findall('^.*"ZRASISTENCIA.*$', l, re.M)
      
        if not rpt:   
            print("No se encontró resultados en el archivo RPT, intentaremos pasar a formato correcto...\n")
            cdata.leer_archivo(data)
            return leer_rpt("transformed.rpt")

        for element in rpt:
            rpt = element.split(" ")
            
            if rpt[1]=="":
                rpt.pop(1)

            rpt[0] = rpt[0].replace(",", "")
            rpt.pop(2)

            t = rpt[1].split(":")
            hora = int(t[0])
            minuto = t[1]
            segundo = t[2]

            hora = hora + 4

            if hora >= 24:
                hora = abs(24- hora)
                fecha = rpt[0].split("/")
                year = fecha[0]
                month = fecha[1]
                day = int(fecha[2])
                day = day + 1
                fecha = str(year)+"/"+str(month)+"/"+str(day)
                rpt[0] = fecha

            nt =str(hora) + ":" + minuto + ":" + segundo
            rpt[1] = nt
            rpt_total.append(rpt)

            if len(rpt) == 5:
                rpt[2] = rpt[2]+rpt[3]
                rpt.pop(3)

    sessions = defaultdict(list)
    for event in rpt_total:
        sessions[event[2]].append(event)
    
    for y in sessions.values():
        eventos = int(len(y))
        contador = 0

        while contador != eventos:
            y[contador].pop(2)
            contador += 1
    
    return sessions

def calculo_tiempo(data_total):
    """Lee en todas las sesiones de juego que registra el RPT y suma el tiempo total de juego, luego lo compara con el tiempo que debería haber estado activo y 
    revela si su asistencia es válida o no, además de haber atraso lo acusa al final.

Retorna un diccionario de formato tt = {jugador: [calculo_tiempo, asistencia, atraso]}"""
    
    tt = {}
    for x, y in data_total.items():
        eventos = int(len(y))
        contador = 0
        total_time = datetime.timedelta(hours=0, minutes=0, seconds=0)

        hora_ingreso = y[0][1]
        hora_ingreso = hora_ingreso.split(":")
        segundo_ingreso = int(hora_ingreso[2])
        minuto_ingreso  = int(hora_ingreso[1])
        hora_ingreso    = int(hora_ingreso[0])

        hora_ingreso = datetime.timedelta(hours=hora_ingreso, minutes= minuto_ingreso, seconds= segundo_ingreso)
        if hora_ingreso > datetime.timedelta(hours=21, minutes=15, seconds=0):
            atrasado = True
        else:
            atrasado = False

        while contador != eventos:
            try:
                date_in = y[contador][0].split("/")
                year_in = int(date_in[0])
                month_in = int(date_in[1])
                day_in = int(date_in[2])
                time_in = y[contador][1].split(":")
                hour_in = int(time_in[0])
                minute_in = int(time_in[1])
                second_in = int(time_in[2])
            except IndexError:
                print("ERROR: No encontré conexión de " + x + "\n")
                break
            try:
                date_out = y[contador+1][0].split("/")
                year_out = int(date_out[0])
                month_out = int(date_out[1])
                day_out = int(date_out[2])
                time_out = y[contador+1][1].split(":")
                hour_out = int(time_out[0])
                minute_out = int(time_out[1])
                second_out = int(time_out[2])
            except IndexError:
                print("ERROR: No encontré desconexión de " + x + ".\n¿Seguirá conectado?\n")
                conectados.append(x)

            in_time = datetime.datetime(year_in, month_in, day_in, hour_in, minute_in, second_in)
            out_time = datetime.datetime(year_out, month_out, day_out, hour_out, minute_out, second_out)

            duration_time = abs(out_time - in_time)
            total_time = duration_time + total_time

            contador +=2

        tiempo_asistencia = datetime.timedelta(hours=1, minutes=20)
        tiempo_minimo     = datetime.timedelta(minutes=30)

        if total_time >= tiempo_asistencia:
            asistencia = "asiste"
        elif total_time <= tiempo_asistencia and total_time > tiempo_minimo:
            asistencia = "media asistencia"
        else:
            asistencia = "falta"
            print("\n"+ x + " no tiene suficiente tiempo de juego para considerarlo asistencia...")
            print("¿Quizás " + x + " tuvo falla de conexión?\n")
        
        tt.setdefault(x, []).append("tiempo de sesión: "+ str(total_time))
        tt.setdefault(x, []).append(asistencia)
        
        if atrasado:
            tt.setdefault(x, []).append("Atrasado: " + str(hora_ingreso))
    
    return tt

def actualmente_conectado(jugador):
    """Agrega jugadores a la lista de jugadores conectados cada vez que calculo_tiempo() falla en encontrar un evento de desconexión.

Retorna una lista con todos los jugadores actualmente conectados"""

    conectados.append(jugador)

    return conectados


def generaReporte(asistenciaDict):
    """" Lee el .txt con la lista de miembros activos y la compara con el diccionario de asistencia generado.
    Crea un .txt reportando los resultados en un formato humano legible """

    # genera la lista de miembros a partir del .txt, quito el caracter newline y le pongo FALTA como valor default
    with open(settings.BASE_DIR+'\\asistencia\\ArmaStats\\'+"listaZR.txt", "r") as f:
        listaZR = []
        for line in f:
            jugador = {'nombre': line.strip('\n'), 'asistencia': "falta", 'tiempo': "---"}
            listaZR.append(jugador)

    server = asistenciaDict.pop("__SERVER__") #quito el server de la lista de jugadores

    for jugadorLista in listaZR:
        for jugador, asistencia in asistenciaDict.items():
            j1 = jugador.split('.', 1)[1]  # toma solo el nombre sin el rango, en el if se pasa a UPPER
            j2 = jugadorLista['nombre'].upper().split(' ', 1)  # toma solo el nombre sin la unidad y lo pasa a UPPER
            if j1.upper() == j2[1]:  # si figura en ambos archivos, es que se conectó al server.
                jugadorLista['asistencia'] = asistencia[1]  # Reemplazo la Falta por la asistencia en ListaZR
                jugadorLista['tiempo'] = asistencia[0]

    # escribo el reporte linea por linea
    i = 1
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    with open(settings.BASE_DIR+'\\asistencia\\ArmaStats\\'+'reporte ('+today+').txt', 'w') as reporte:
        for jugadorLista in listaZR:
            reporte.write(str(i) + ") " + jugadorLista['nombre'] + "  " + jugadorLista['asistencia'] + " " + jugadorLista['tiempo']+"\n")
            i += 1





def main(uploadFile):
    """Launcher."""
    rptdata    = leer_rpt(uploadFile)
    asistencia = calculo_tiempo(rptdata)
    
    if len(conectados) > 0:
        print("\nJugadores conectados: ")
        y = 0
        for jugador in conectados:
            y += 1
            print(str(y)+". " + jugador)
    else:
        print("No hay jugadores conectados\n\n")
    
    print("\nDetalle de asistencia: ")
    for x, y in asistencia.items():
        print(x, y)

    print("-------------------------")
    generaReporte(asistencia)
    return (asistencia)


#if __name__ == "__main__":
#    main()
