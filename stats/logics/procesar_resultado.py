from django.shortcuts import render
from django.http import HttpResponseRedirect
from stats.forms import UploadReporteForm
from stats.logics import procesar_rpt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from stats.models import Miembro, Asistencia, Mision
from datetime import datetime, timedelta
from django.views.generic.list import ListView


def handle_uploaded_file(mision_input):
    mision = Mision(mision_input)
    resultado_rpt = procesar_rpt.main(mision.reporte.path)
    dict_mision = resultado_rpt[0]
    fecha = dict_mision['fecha']
    fecha = datetime.strptime(fecha, '%y:%m:%d')
    miembros = Miembro.objects.all()

    mision.nombre = dict_mision['nombre_mision']
    mision.tipo = dict_mision['tipo_mision']
    mision.nombre_campa = dict_mision['nombre_campa']
    mision.fecha = fecha
    mision.save()

    for miembro in miembros:  # miembro de la lista de la DB
        asiste = Asistencia()
        asiste.mision = mision
        asiste.miembro = miembro
        asiste.fecha = fecha
        asiste.asistencia = 'Falta'
        t = datetime.strptime("0:0:0", '%H:%M:%S')
        delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
        asiste.tiempo_de_sesion = delta
        asiste.save()

        for index in resultado_rpt[1:]:
            dict_jugador = resultado_rpt[index]
            j1 = dict_jugador['nombre']
            j2 = miembro.nombre.upper()
            if j1.upper() == j2:  # si coinciden es que se conectó al server y debo crear un Asistencia
                asiste = Asistencia.objects.get(miembro=miembro, fecha=fecha)
                print("ENCONTRE A "+j1+" LE PONGO ASISTENCIA")
                asiste.asistencia = dict_jugador['asistencia']
                t = datetime.strptime(
                    dict_jugador['tiempo_sesion'], '%H:%M:%S')
                delta = timedelta(
                    hours=t.hour, minutes=t.minute, seconds=t.second)
                asiste.tiempo_de_sesion = delta
                asiste.requiere_atencion = dict_jugador['requiere_atencion']
                # TODO comprobar diferencia en el rango ingame con el del miembro, podemos actualizar rangos aquí
                asiste.save()

