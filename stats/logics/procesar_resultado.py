from stats.logics.classes import rpt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from stats.models import Miembro, Asistencia, Mision, Campana
from datetime import datetime, timedelta

def handle_uploaded_file(mision, override_by_rpt=True):
    mision.save()
    reporte = rpt.RPT(mision.reporte.path)
    dict_rpt = reporte.data_final

    fecha_rpt = dict_rpt["fecha"]
    fecha_rpt = datetime.strptime(fecha_rpt, '%Y/%m/%d')
    mision.fecha_finalizada = fecha_rpt
    mision.estado = Mision.ESTADO_FINALIZADA  # Si subo el reporte si o si tiene que estar FINALIZADA

    if override_by_rpt:
        mision.nombre = dict_rpt["mision"]
        mision.descripcion = dict_rpt["desc"]
        mision.mapa = dict_rpt["mapa"]
        mision.tipo = dict_rpt["tipo"]
        mision.oficial = dict_rpt["oficial"]
        campana_nombre = dict_rpt["nombre_campa"]

        # Si el nombre campaña es None, ni siquiera intento buscar o crear campaña
        if campana_nombre is not None:
            try:
                # busco si existe campaña y si coincide asigno existente
                campana = Campana.objects.get(nombre__iexact=campana_nombre)
                mision.campana = campana
            except Campana.DoesNotExist:
                campana = Campana()
                campana.nombre = campana_nombre
                if dict_rpt['tipo'] == Mision.TIPO_CAMPANA:
                    campana.tipo = Campana.TIPO_CAMPANA
                elif dict_rpt['tipo'] == str(Mision.TIPO_CURSO):
                    campana.tipo = Campana.TIPO_CURSO
                else:
                    campana.tipo = Campana.TIPO_OTRO
                campana.estado = Campana.ESTADO_EN_CURSO
                campana.save()
                mision.campana = campana
        else:
            mision.campana = None

        # busco si el autor coincide con un Miembro
        autor_nombre = dict_rpt['autor']
        try:
            autor = Miembro.objects.get(nombre__iexact=autor_nombre)
            mision.autor = autor
        except Miembro.DoesNotExist:
            autor = Miembro.objects.get(nombre__iexact="TECDI")
            mision.autor = autor
        # TODO subir imagen default / tomar imagen del pbo

    mision.save()
    miembros = Miembro.objects.all()
    total_asistencias = dict_rpt["asistencias"]
    for miembro in miembros: #miembros en la DB
        asiste = Asistencia()
        if miembro.rango.abreviatura == 'Asp':
            asiste.requiere_atencion = True
        asiste.mision = mision
        asiste.miembro = miembro
        asiste.fecha = fecha_rpt
        asiste.asistencia = Asistencia.ASIST_FALTA
        asiste.mensaje_notificacion = ""
        t = datetime.strptime("0:0:0", '%H:%M:%S')
        delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
        asiste.tiempo_de_sesion = delta
        asiste.save()


        for elemento in total_asistencias:
            j1 = elemento["nombre"]
            j2 = miembro.nombre.upper()
            if j1.upper() == j2:  # si coinciden es que se conectó al server y debo crear un Asistencia
                asiste = Asistencia.objects.get(miembro=miembro, fecha=fecha_rpt)
                print("ENCONTRE A "+j1+" LE PONGO ASISTENCIA")
                asiste.requiere_atencion = elemento["requiere_atencion"]
                # Si FALTA me fijo si está en licencia o reserva
                if elemento["asistencia"].lower() == Asistencia.ASIST_FALTA.lower():
                    asiste.asistencia = Asistencia.ASIST_FALTA
                    if miembro.estado == Miembro.ESTADO_LICENCIA:
                        asiste.asistencia = Asistencia.ASIST_LICENCIA
                    if miembro.estado == Miembro.ESTADO_RESERVA:
                        asiste.asistencia = Asistencia.ASIST_RESERVA
                # Si TARDE me fijo si está en licencia o reserva (para notificar)
                elif elemento["asistencia"].lower() == Asistencia.ASIST_TARDE.lower():
                    asiste.asistencia = Asistencia.ASIST_TARDE
                    if miembro.estado == Miembro.ESTADO_LICENCIA:
                        asiste.requiere_atencion = True
                        asiste.mensaje_notificacion = asiste.mensaje_notificacion + "\n" \
                                                    + miembro.nombre + ": No estaba de Licencia?"
                    if miembro.estado == Miembro.ESTADO_RESERVA:
                        asiste.requiere_atencion = True
                        asiste.mensaje_notificacion = asiste.mensaje_notificacion + "\n" \
                                                    + miembro.nombre + ": No estaba en Reserva?"

                # Si ASISTE me fijo si está en licencia o reserva (para notificar)
                elif elemento["asistencia"].lower() == Asistencia.ASIST_ASISTE.lower():
                    asiste.asistencia = Asistencia.ASIST_ASISTE
                    if miembro.estado == Miembro.ESTADO_LICENCIA:
                        asiste.requiere_atencion = True
                        asiste.mensaje_notificacion = asiste.mensaje_notificacion + "\n" \
                                                    + miembro.nombre + ": No estaba de Licencia?"
                    if miembro.estado == Miembro.ESTADO_RESERVA:
                        asiste.requiere_atencion = True
                        asiste.mensaje_notificacion = asiste.mensaje_notificacion + "\n" \
                                                    + miembro.nombre + ": No estaba en Reserva?"

                # El reporte nunca viene con JUSTIFICADA, no debería llegar aca
                elif elemento["asistencia"].lower() == Asistencia.ASIST_JUSTIFICADA.lower():
                    asiste.asistencia = Asistencia.ASIST_JUSTIFICADA

                # El reporte nunca viene con LICENCIA, no debería llegar aca
                elif elemento["asistencia"].lower() == Asistencia.ASIST_LICENCIA.lower():
                    asiste.asistencia = Asistencia.ASIST_LICENCIA

                # El reporte nunca viene con RESERVA, no debería llegar aca
                elif elemento["asistencia"].lower() == Asistencia.ASIST_RESERVA.lower():
                    asiste.asistencia = Asistencia.ASIST_RESERVA

                else:
                    asiste.asistencia = "Oops!"  # Nunca debería llegar acá

                # Le pongo la duración de la sesión
                t = datetime.strptime(elemento["tiempo_sesion"], '%H:%M:%S')
                delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
                asiste.tiempo_de_sesion = delta

                # TODO comprobar diferencia en el rango ingame con el del miembro, podemos actualizar rangos aquí
                if elemento["rango"].lower() != miembro.rango.abreviatura.lower():
                    asiste.requiere_atencion = True
                    asiste.mensaje_notificacion = asiste.mensaje_notificacion + "\n" \
                                                + miembro.nombre + ": Comprobar rango." \
                                                + ". En sistema: " + miembro.rango.abreviatura \
                                                + ". En reporte: " + elemento['rango'] + "."

                asiste.save()

