from stats.logics import procesar_rpt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from stats.models import Miembro, Asistencia, Mision, Campana
from datetime import datetime, timedelta


def handle_uploaded_file(mision, override_by_rpt=True):
    mision.save()  # tengo que guardar primero la mision para que se guarde el rpt y me tome el File
    resultado_rpt = procesar_rpt.main(mision.reporte.path)
    dict_mision = resultado_rpt[0]
    fecha_rpt = dict_mision['fecha']
    fecha_rpt = datetime.strptime(fecha_rpt, '%Y/%m/%d')
    mision.fecha_finalizada = fecha_rpt
    mision.estado = Mision.ESTADO_FINALIZADA  # Si subo el reporte si o si tiene que estar FINALIZADA

    if override_by_rpt:  # asumo Form inexistente y trato de llenar todolo que pueda desde el rpt
        mision.nombre = dict_mision['NOMBRE_MISION']
        mision.descripcion = dict_mision['DESC_MISION']
        mision.mapa = dict_mision['MAPA_MISION']
        mision.tipo = dict_mision['TIPO_MISION']
        if dict_mision['ES_OFICIAL'] == "True":
            mision.oficial = True
        else:
            mision.oficial = False
        campana_nombre = dict_mision['NOMBRE_CAMPA']
        # Si el nombre campaña es None, ni siquiera intento buscar o crear campaña
        if campana_nombre is not None:
            try:
                # busco si existe campaña y si coincide asigno existente
                campana = Campana.objects.get(nombre__iexact=campana_nombre)
                mision.campana = campana
            except Campana.DoesNotExist:
                # si no existe, creo una campaña nueva
                campana = Campana()
                campana.nombre = campana_nombre
                if dict_mision['TIPO_MISION'] == Mision.TIPO_CAMPANA:
                    campana.tipo = Campana.TIPO_CAMPANA
                elif dict_mision['TIPO_MISION'] == str(Mision.TIPO_CURSO):
                    campana.tipo = Campana.TIPO_CURSO
                else:
                    campana.tipo = Campana.TIPO_OTRO
                campana.estado = Campana.ESTADO_EN_CURSO
                campana.save()
                mision.campana = campana
        else:
            mision.campana = None

        # busco si el autor coincide con un Miembro
        autor_nombre = dict_mision['AUTOR_MISION']
        try:
            autor = Miembro.objects.get(nombre__iexact=autor_nombre)
            mision.autor = autor
        except Miembro.DoesNotExist:
            pass
        # TODO subir imagen default / tomar imagen del pbo

    mision.save()
    resultado_rpt.pop(0)  # elminio el primer elemento del dict (el que NO es una asistencia)
    miembros = Miembro.objects.all()
    for miembro in miembros:  # miembro de la lista de la DB
        asiste = Asistencia()
        if miembro.rango.abreviatura == 'Asp':
            asiste.requiere_atencion = True
        asiste.mision = mision
        asiste.miembro = miembro
        asiste.fecha = fecha_rpt
        asiste.asistencia = 'Falta'
        t = datetime.strptime("0:0:0", '%H:%M:%S')
        delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
        asiste.tiempo_de_sesion = delta
        asiste.save()

        for index in resultado_rpt:
            dict_jugador = index
            j1 = dict_jugador['nombre']
            j2 = miembro.nombre.upper()
            if j1.upper() == j2:  # si coinciden es que se conectó al server y debo crear un Asistencia
                asiste = Asistencia.objects.get(miembro=miembro, fecha=fecha_rpt)
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
