from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadReporteForm
from .logics import procesar_resultado
from .models import Clase, Rango, Nacionalidad, Rol, Unidad, Miembro, Mision, Asistencia, User, Campana, MisionGaleria
from .logics import services
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.views.generic.base import RedirectView
from .forms import ClaseForm, RangoForm, NacionalidadForm, RolForm, UnidadForm, MiembroForm, MisionForm, \
    AsistenciaForm, CampanaForm, MisionReporteForm, MisionGaleriaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.utils import timezone
import calendar
from django.core.paginator import Paginator
import random


def index_view(request):
    context = {}
    context['fondo'] = random.randint(1, 11)
    context['hide_title_bar'] = True
    context['hide_left_bar'] = True
    context['navbartop_sin_header'] = True
    context['margin_cero_inner_wrapper'] = True
    context['mision_list'] = services.genera_calendario()

    return render(request, 'stats/index.html', context)


class TestPage(ListView):
    template_name = 'stats/test_page.html'
    model = Miembro

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from django.core.management import call_command
        # call_command('datos_iniciales')
        return context


# Vista para crear un MisionGaleria luego de subir imagen a Imgur
class RedirectMisionGaleria(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        mision = Mision.objects.get(id=self.kwargs['mision_id'])
        miembro = Miembro.objects.get(id=self.kwargs['miembro_id'])
        url = "https://i.imgur.com/" + self.kwargs['image']
        MisionGaleria.objects.create(mision=mision, imagen_url=url, miembro=miembro)
        return reverse('stats:mision_detail', kwargs={'pk': self.kwargs['mision_id']})


# Vista para redireccionar al user a su propio perfil
class RedirectToProfile(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
            miembro = Miembro.objects.get(user_id=user_id)
            return reverse('stats:profile', kwargs={'pk': miembro.id})
        else:
            reverse('stats:index')


# Vista para renderizar el perfil de alguien
class MyProfileView(LoginRequiredMixin, DetailView):
    template_name = 'stats/profile.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(id=self.kwargs['pk'])
        miembro = user.miembro
        context['hide_left_bar'] = True
        return context


class PublicProfileView(DetailView):
    template_name = 'stats/profile.html'
    model = Miembro

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        miembro = Miembro.objects.get(id=self.kwargs['pk'])
        hoy = timezone.now()
        asistencia_mensual = []
        for i in range(12):
            mes = None
            mes = miembro.get_asistencia_del_mes(i + 1, 2019)
            if mes.count() > 0:
                asistencia_mensual.append(mes)
        context['asistencia_mensual'] = asistencia_mensual
        context['hide_left_bar'] = True
        context['fondo'] = random.randint(1, 11)

        campanas_asistidas = miembro.campanas_asistidas()
        campanas = []
        for camp in campanas_asistidas:
            camp_tupla = {}
            camp_tupla['campana'] = camp
            camp_tupla['asistencias'] = miembro.asistencia_en_campana(camp.id)
            camp_tupla['porcentaje'] = services.calcula_porcentaje(miembro.asistencia_en_campana(camp.id),
                                                                   camp.mision_set.count())
            campanas.append(camp_tupla)

        context['campanas_asistidas'] = campanas
        context['total_campana'] = Mision.objects.filter(tipo=Mision.TIPO_CAMPANA).count()
        context['total_improvisada'] = Mision.objects.filter(tipo=Mision.TIPO_IMPROVISADA).count()
        context['total_gala'] = Mision.objects.filter(tipo=Mision.TIPO_GALA).count()
        context['total_entrenamiento'] = Mision.objects.filter(tipo=Mision.TIPO_ENTRENAMIENTO).count()
        context['total_otro'] = Mision.objects.filter(tipo=Mision.TIPO_OTRO).count()
        context['total_curso'] = Mision.objects.filter(tipo=Mision.TIPO_CURSO).count()
        context['total_cooperativa'] = Mision.objects.filter(tipo=Mision.TIPO_COOPERATIVA).count()

        context['porc_campana'] = services.calcula_porcentaje(miembro.get_asistencia_tipo_campana().count(),
                                                              context['total_campana'])

        context['porc_improvisada'] = services.calcula_porcentaje(miembro.get_asistencia_tipo_improvisada().count(),
                                                                  context['total_improvisada'])

        context['porc_gala'] = services.calcula_porcentaje(miembro.get_asistencia_tipo_gala().count(),
                                                           context['total_gala'])

        context['porc_entrenamiento'] = services.calcula_porcentaje(miembro.get_asistencia_tipo_entrenamiento(),
                                                                    context['total_entrenamiento'])

        context['porc_otro'] = services.calcula_porcentaje(miembro.get_asistencia_tipo_otro().count(),
                                                           context['total_otro'])

        context['porc_curso'] = services.calcula_porcentaje(miembro.get_asistencia_tipo_curso().count(),
                                                            context['total_curso'])

        context['porc_cooperativa'] = services.calcula_porcentaje(miembro.get_asistencia_tipo_cooperativa().count(),
                                                                  context['total_cooperativa'])

        return context


# Vista para el formulario de crear misiones
class CrearMision(CreateView):
    template_name = 'stats/mision/mision_create_form.html'
    model = Mision
    form_class = MisionForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        mision = self.object
        if mision.reporte:
            # override_by_rpt le da prioridad a los datos del rpt
            procesar_resultado.handle_uploaded_file(mision, override_by_rpt=True)
        else:
            # mision.notas_privadas = "SIN REPORTE"
            pass
        mision.save()
        return super(CrearMision, self).form_valid(form)


# Vista para el formulario de SUBIR REPORTE y crear la misión automáticamente
class CrearMisionReporte(CreateView):
    template_name = 'stats/mision/mision_reporte_create_form.html'
    model = Mision
    form_class = MisionReporteForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        mision = self.object
        if mision.reporte:
            # override_by_rpt le da prioridad a los datos del rpt
            procesar_resultado.handle_uploaded_file(mision, override_by_rpt=True)
        else:
            # redireccionar error upload reporte
            pass
        mision.save()
        return super(CrearMisionReporte, self).form_valid(form)


class ActualizarMision(UpdateView):
    template_name = 'stats/mision/mision_create_form.html'
    model = Mision
    form_class = MisionForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        mision = self.object
        if mision.reporte is None:
            # Subo reporte nuevo
            # override_by_rpt le da prioridad a los datos del rpt
            procesar_resultado.handle_uploaded_file(mision, override_by_rpt=False)
        else:
            # ya tenia reporte desde antes no tengo que procesar nada
            pass
        mision.save()
        return super(ActualizarMision, self).form_valid(form)


class CalendarView(ListView):
    template_name = 'stats/calendario.html'
    model = Mision

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mision_list'] = services.genera_calendario()
        return context


class AsistenciaMes(ListView):
    template_name = 'stats/asistencia_mes.html'
    model = Mision

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        miembros = Miembro.objects.all().order_by('rango__orden', 'nombre')
        year = self.kwargs['year']
        month = self.kwargs['month']
        misiones_mes = Mision.objects.filter(oficial=True, fecha_finalizada__year=year,
                                             fecha_finalizada__month=month).order_by('fecha_finalizada', 'id')


        # Hago calculos de Datetime para obtener mes actual, mes anterior y mes siguiente
        fecha_mes = datetime(year, month, 1)  # Fecha de la URL
        ultimo_dia_del_mes_actual = fecha_mes.replace(day=28) + timedelta(days=4)
        ultimo_dia_del_mes_actual = ultimo_dia_del_mes_actual - timedelta(days=ultimo_dia_del_mes_actual.day)

        lista_asistencia = []
        for m in miembros:
            asist_miem = services.asistencia_miembro(m, month, year)
            lista_asistencia.append(asist_miem)

        context['asistencia'] = lista_asistencia
        context['misiones_mes'] = misiones_mes
        context['unidades'] = Unidad.objects.all()
        context['fecha_mes'] = datetime(year, month, 1)
        context['fecha_mes_anterior'] = fecha_mes - timedelta(days=1)
        context['fecha_mes_posterior'] = ultimo_dia_del_mes_actual + timedelta(days=1)
        context['fecha_mes_actual'] = datetime.today()
        return context


def asistencia_datatables_ajax(request, year, month):
    miembros = Miembro.objects.all().order_by('rango__orden', 'nombre')
    misiones_mes = Mision.objects.filter(oficial=True, fecha_finalizada__year=year,
                                         fecha_finalizada__month=month).order_by('fecha_finalizada', 'id')

    lista_asistencia = []
    for m in miembros:
        asist_miem = services.asistencia_miembro(m, month, year)
        lista_asistencia.append(asist_miem)

    paginator = Paginator(lista_asistencia, request.GET.get('page_length', 25))  # Show 25 contacts per page

    page = request.GET.get('page')  # Add option in ajax or somewhere
    all_asistencia_list = paginator.get_page(page)  # Return objects list you can make json from this or list

    return JsonResponse(all_asistencia_list, safe=False)


# ======================================================================================================================
#                      Funciones CRUD (Create, Read, Update and Delete) básicas de los Models
# ======================================================================================================================

class ClaseListView(ListView):
    template_name = 'stats/crud/clase_list.html'
    model = Clase


class ClaseCreateView(CreateView):
    template_name = 'stats/crud/clase_form.html'
    model = Clase
    form_class = ClaseForm


class ClaseDetailView(DetailView):
    template_name = 'stats/crud/clase_detail.html'
    model = Clase


class ClaseUpdateView(UpdateView):
    template_name = 'stats/crud/clase_form.html'
    model = Clase
    form_class = ClaseForm


class RangoListView(ListView):
    template_name = 'stats/crud/rango_list.html'
    model = Rango


class RangoCreateView(CreateView):
    template_name = 'stats/crud/rango_form.html'
    model = Rango
    form_class = RangoForm


class RangoDetailView(DetailView):
    template_name = 'stats/crud/rango_detail.html'
    model = Rango


class RangoUpdateView(UpdateView):
    template_name = 'stats/crud/rango_form.html'
    model = Rango
    form_class = RangoForm


class NacionalidadListView(ListView):
    template_name = 'stats/crud/nacionalidad_list.html'
    model = Nacionalidad


class NacionalidadCreateView(CreateView):
    template_name = 'stats/crud/nacionalidad_form.html'
    model = Nacionalidad
    form_class = NacionalidadForm


class NacionalidadDetailView(DetailView):
    template_name = 'stats/crud/nacionalidad_detail.html'
    model = Nacionalidad


class NacionalidadUpdateView(UpdateView):
    template_name = 'stats/crud/nacionalidad_form.html'
    model = Nacionalidad
    form_class = NacionalidadForm


class RolListView(ListView):
    template_name = 'stats/crud/rol_list.html'
    model = Rol


class RolCreateView(CreateView):
    template_name = 'stats/crud/rol_form.html'
    model = Rol
    form_class = RolForm


class RolDetailView(DetailView):
    template_name = 'stats/crud/rol_detail.html'
    model = Rol


class RolUpdateView(UpdateView):
    template_name = 'stats/crud/rol_form.html'
    model = Rol
    form_class = RolForm


class UnidadListView(ListView):
    template_name = 'stats/crud/unidad_list.html'
    model = Unidad


class UnidadCreateView(CreateView):
    template_name = 'stats/crud/unidad_form.html'
    model = Unidad
    form_class = UnidadForm


class UnidadDetailView(DetailView):
    template_name = 'stats/crud/unidad_detail.html'
    model = Unidad


class UnidadUpdateView(UpdateView):
    template_name = 'stats/crud/unidad_form.html'
    model = Unidad
    form_class = UnidadForm


class CampanaListView(ListView):
    template_name = 'stats/crud/campana_list.html'
    model = Campana


class CampanaCreateView(CreateView):
    template_name = 'stats/crud/campana_form.html'
    model = Campana
    form_class = CampanaForm


class CampanaDetailView(DetailView):
    template_name = 'stats/crud/campana_detail.html'
    model = Campana


class CampanaUpdateView(UpdateView):
    template_name = 'stats/crud/campana_form.html'
    model = Campana
    form_class = CampanaForm


class MiembroListView(ListView):
    template_name = 'stats/crud/miembro_list.html'
    model = Miembro

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paises = Nacionalidad.objects.raw(
            'SELECT * FROM stats_nacionalidad JOIN stats_miembro on stats_miembro.nacionalidad_id = stats_nacionalidad.id GROUP BY pais')
        context['paises'] = paises
        context['unidades'] = Unidad.objects.all()
        return context


class MiembroCreateView(CreateView):
    template_name = 'stats/crud/miembro_form.html'
    model = Miembro
    form_class = MiembroForm


class MiembroDetailView(DetailView):
    template_name = 'stats/crud/miembro_detail.html'
    model = Miembro

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fecha'] = datetime.today()
        return context


class MiembroUpdateView(UpdateView):
    template_name = 'stats/crud/miembro_form.html'
    model = Miembro
    form_class = MiembroForm


class MisionListView(ListView):
    template_name = 'stats/crud/mision_list.html'
    model = Mision
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MisionCreateView(CreateView):
    template_name = 'stats/crud/mision_form.html'
    model = Mision
    form_class = MisionForm


class MisionDetailView(DetailView):
    template_name = 'stats/crud/mision_detail.html'
    model = Mision

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imagenes_galeria'] = MisionGaleria.objects.filter(mision__id=self.kwargs['pk'])
        context['unidades'] = Unidad.objects.all().order_by('nombre')
        context['hide_left_bar'] = True
        context['fondo'] = random.randint(1, 11)
        return context


class MisionUpdateView(UpdateView):
    template_name = 'stats/crud/mision_form.html'
    model = Mision
    form_class = MisionForm


class MisionDeleteView(DeleteView):
    model = Mision
    success_url = reverse_lazy('stats:mision_list')
    template_name = 'stats/crud/mision_confirm_delete.html'


class AsistenciaListView(ListView):
    template_name = 'stats/crud/asistencia_list.html'
    model = Asistencia


class AsistenciaCreateView(CreateView):
    template_name = 'stats/crud/asistencia_form.html'
    model = Asistencia
    form_class = AsistenciaForm


class AsistenciaDetailView(DetailView):
    template_name = 'stats/crud/asistencia_detail.html'
    model = Asistencia


class AsistenciaUpdateView(UpdateView):
    template_name = 'stats/crud/asistencia_form.html'
    model = Asistencia
    form_class = AsistenciaForm


class MisionGaleriaCreateView(CreateView):
    template_name = 'stats/crud/misiongaleria_form.html'
    model = MisionGaleria
    form_class = MisionGaleriaForm


class MisionGaleriaDetailView(DetailView):
    template_name = 'stats/crud/misiongaleria_detail.html'
    model = MisionGaleria


class MisionGaleriaUpdateView(UpdateView):
    template_name = 'stats/crud/misiongaleria_form.html'
    model = MisionGaleria
    form_class = MisionGaleriaForm


class MisionGaleriaListView(ListView):
    template_name = 'stats/crud/misiongaleria_list.html'
    model = MisionGaleria


# ESTAS FUNCIONES COMENTADAS LAS GUARDO SOLO COMO REFERENCIA/DOCUMENTACION

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadReporteForm(request.POST, request.FILES)
#         if form.is_valid():
#             mision = Mision(reporte=request.FILES['file'])
#             procesar_resultado.handle_uploaded_file(mision)
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadReporteForm()
#     return render(request, 'stats/upload.html', {'form': form})


# class AsistenciaListView(ListView):
#     template_name = 'stats/tabla_asistencia.html'
#     model = Asistencia
#     paginate_by = 100  # if pagination is desired
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['miembros'] = Miembro.objects.all()
#         context['reportes'] = Mision.objects.all()
#         return context
