from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadReporteForm
from .logics import procesar_rpt
from .logics import procesar_resultado
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Miembro, Asistencia, Mision
from datetime import datetime, timedelta
from django.views.generic.list import ListView


def index_view(request):
    return render(request, 'stats/index.html', {})

# TODO hacer esta función más linda


def upload_file(request):
    if request.method == 'POST':
        form = UploadReporteForm(request.POST, request.FILES)
        if form.is_valid():
            # mision = Mision(reporte=request.FILES['file'])
            # mision.nombre = "Test"
            # mision.tipo = "Otros"
            # mision.nombre_campa = "Campaña"
            # mision.fecha = datetime.today().strftime('%Y-%m-%d')
            # mision.save()
            #file = request.FILES['file']
            #path = default_storage.save(str(mision.mision), ContentFile(mision.mision.read()))
            #dict = zrasistencia.main_django(mision.mision.path)
            #dict = armastats.main(mision.mision.path)

            print("Comienza analisis-----")
            mision = Mision(reporte=request.FILES['file'])
            procesar_resultado(mision)
            #####################################################
            # - - - - - - - - - - - - - - - - - - cortar aquí
            #####################################################
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
                delta = timedelta(
                    hours=t.hour, minutes=t.minute, seconds=t.second)
                asiste.tiempo_de_sesion = delta
                asiste.save()
                #print("Estoy en miembro: "+miembro.nombre)
                # for jugador, asistencia in dict.items():  # el dict retornado por el script
                #     #print("Estoy en JUGADOR: " + jugador.split('.', 1)[1])
                #     j1 = jugador.split('.', 1)[1]  # toma solo el nombre sin el rango, en el if se pasa a UPPER
                #     j2 = miembro.nombre.upper()  # toma el nombre de Miembro y lo pasa a UPPER
                #     if j1.upper() == j2:  # si coinciden es que se conectó al server y debo crear un Asistencia
                #         asiste = Asistencia.objects.get(miembro=miembro, fecha=datetime.today().strftime('%Y-%m-%d'))
                #         print("ENCONTRE A "+j1+" LE PONGO ASISTENCIA")
                #         asiste.asistencia = asistencia[1]
                #         t = datetime.strptime(asistencia[0], '%H:%M:%S')
                #         delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
                #         asiste.tiempo_de_sesion = delta
                #         #asiste.requiere_atencion = False
                #         asiste.save()

                for index in resultado_rpt[1:len(resultado_rpt)]:
                    dict_jugador = resultado_rpt[index]
                    j1 = dict_jugador['nombre']
                    j2 = miembro.nombre.upper()
                    if j1.upper() == j2:  # si coinciden es que se conectó al server y debo crear un Asistencia
                        asiste = Asistencia.objects.get(
                            miembro=miembro, fecha=fecha)
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
            #####################################################
            # - - - - - - - - - - - - - - - - - - cortar aquí
            #####################################################

            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadReporteForm()
    return render(request, 'stats/upload.html', {'form': form})


class AsistenciaListView(ListView):
    template_name = 'stats/tabla_asistencia.html'
    model = Asistencia
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['miembros'] = Miembro.objects.all()
        context['reportes'] = Mision.objects.all()
        return context
