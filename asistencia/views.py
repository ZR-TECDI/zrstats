from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadReporteForm
from .ArmaStats import armastats, zrasistencia
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Miembro, Asistencia, Mision
from datetime import datetime, timedelta
from django.views.generic.list import ListView


def index_view(request):
    return render(request, 'asistencia/index.html', {})


def upload_file(request):
    if request.method == 'POST':
        form = UploadReporteForm(request.POST, request.FILES)
        if form.is_valid():
            reporte = Mision(reporte=request.FILES['file'])
            reporte.fecha = datetime.today().strftime('%Y-%m-%d')
            reporte.save()
            #file = request.FILES['file']
            #path = default_storage.save(str(reporte.reporte), ContentFile(reporte.reporte.read()))
            #dict = zrasistencia.main_django(reporte.reporte.path)
            dict = armastats.main(reporte.reporte.path)
            miembros = Miembro.objects.all()

            print("Comienza analisis-----")
            for miembro in miembros:  # miembro de la lista de la DB
                asiste = Asistencia()
                asiste.mision = reporte
                asiste.miembro = miembro
                asiste.fecha = datetime.today().strftime('%Y-%m-%d')
                asiste.asistencia = 'Falta'
                t = datetime.strptime("0:0:0", '%H:%M:%S')
                delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
                asiste.tiempo_de_sesion = delta
                asiste.save()
                #print("Estoy en miembro: "+miembro.nombre)
                for jugador, asistencia in dict.items():  # el dict retornado por el script
                    #print("Estoy en JUGADOR: " + jugador.split('.', 1)[1])
                    j1 = jugador.split('.', 1)[1]  # toma solo el nombre sin el rango, en el if se pasa a UPPER
                    j2 = miembro.nombre.upper()  # toma el nombre de Miembro y lo pasa a UPPER
                    if j1.upper() == j2:  # si coinciden es que se conectó al server y debo crear un Asistencia
                        asiste = Asistencia.objects.get(miembro=miembro, fecha=datetime.today().strftime('%Y-%m-%d'))
                        print("ENCONTRE A "+j1+" LE PONGO ASISTENCIA")
                        asiste.asistencia = asistencia[1]
                        t = datetime.strptime(asistencia[0], '%H:%M:%S')
                        delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
                        asiste.tiempo_de_sesion = delta
                        #asiste.requiere_atencion = False
                        asiste.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadReporteForm()
    return render(request, 'asistencia/upload.html', {'form': form})


class AsistenciaListView(ListView):
    template_name = 'asistencia/tabla_asistencia.html'
    model = Asistencia
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['miembros'] = Miembro.objects.all()
        context['reportes'] = Mision.objects.all()
        return context