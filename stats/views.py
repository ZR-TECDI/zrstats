from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadReporteForm
from .logics import procesar_resultado
from .models import Clase, Rango, Nacionalidad, Rol, Unidad, Miembro, Mision, Asistencia, User, Campana
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.views.generic.base import RedirectView
from .forms import ClaseForm, RangoForm, NacionalidadForm, RolForm, UnidadForm, MiembroForm, MisionForm, AsistenciaForm, CampanaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse
from datetime import datetime
import calendar


def index_view(request):
    return render(request, 'stats/index.html', {})


class TestPage(ListView):
    template_name = 'stats/test_page.html'
    model = Miembro


# Vista para redireccionar al user a su propio perfil
class RedirectToProfile(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
            return reverse('stats:profile', kwargs={'pk': user_id})
        else:
            reverse('stats:index')


# Vista para renderizar el perfil de alguien
class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'stats/profile.html'
    model = Miembro


# Vista para el formulario de crear misiones
class CrearMision(CreateView):
    template_name = 'stats/mision_create_form.html'
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


class ActualizarMision(UpdateView):
    template_name = 'stats/mision_create_form.html'
    model = Mision
    form_class = MisionForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        mision = self.object
        if mision.reporte:
            # override_by_rpt le da prioridad a los datos del rpt
            procesar_resultado.handle_uploaded_file(mision, override_by_rpt=False)
        else:
            #mision.notas_privadas = "SIN REPORTE"
            pass
        mision.save()
        return super(ActualizarMision, self).form_valid(form)


class AsistenciaMes(ListView):
    template_name = 'stats/asistencia_mes.html'
    model = Mision

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        miembros = Miembro.objects.all()
        #year = datetime.now().year
        #month = datetime.now().month
        year = self.kwargs['year']
        month = self.kwargs['month']
        month_days = calendar.monthcalendar(year, month)
        misiones_mes = Mision.objects.filter(oficial=True, fecha_finalizada__year=year, fecha_finalizada__month=month)
        asistencia_mensual = Asistencia.objects.filter(fecha__month=month)

        # Armo el calendario del mes
        mision_calendar = []
        for week in month_days:
            for day in week:
                if day != 0:
                    mision_day = {}
                    mision_day["mision"] = None
                    mision_day["day"] = day
                    mision_calendar.append(mision_day)

        # Le pongo misiones a los dias del calendario
        for day in mision_calendar:
            for mision in misiones_mes:
                if mision.fecha_finalizada.day == day["day"]:
                    mision_day = {}
                    idx = mision_calendar.index(day)
                    mision_day["mision"] = mision
                    mision_day["day"] = day["day"]
                    mision_calendar[idx] = mision_day

        context['mision_calendar'] = mision_calendar
        context['misiones_mes'] = misiones_mes
        context['miembros'] = miembros
        context['asistencia'] = asistencia_mensual
        context['fecha_mes'] = datetime(year, month, 1)
        return context


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


class MiembroCreateView(CreateView):
    template_name = 'stats/crud/miembro_form.html'
    model = Miembro
    form_class = MiembroForm


class MiembroDetailView(DetailView):
    template_name = 'stats/crud/miembro_detail.html'
    model = Miembro


class MiembroUpdateView(UpdateView):
    template_name = 'stats/crud/miembro_form.html'
    model = Unidad
    form_class = MiembroForm


class MisionListView(ListView):
    template_name = 'stats/crud/mision_list.html'
    model = Mision


class MisionCreateView(CreateView):
    template_name = 'stats/crud/mision_form.html'
    model = Mision
    form_class = MisionForm


class MisionDetailView(DetailView):
    template_name = 'stats/crud/mision_detail.html'
    model = Mision


class MisionUpdateView(UpdateView):
    template_name = 'stats/crud/mision_form.html'
    model = Mision
    form_class = MisionForm


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

