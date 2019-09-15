from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadReporteForm
from .logics import procesar_resultado
from .models import Clase, Rango, Nacionalidad, Rol, Unidad, Miembro, Mision, Asistencia
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .forms import ClaseForm, RangoForm, NacionalidadForm, RolForm, UnidadForm, MiembroForm, MisionForm, AsistenciaForm


def index_view(request):
    return render(request, 'stats/index.html', {})


# TODO hacer esta función más linda
def upload_file(request):
    if request.method == 'POST':
        form = UploadReporteForm(request.POST, request.FILES)
        if form.is_valid():
            mision = Mision(reporte=request.FILES['file'])
            procesar_resultado.handle_uploaded_file(mision)
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadReporteForm()
    return render(request, 'stats/upload.html', {'form': form})


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
    form_class = UnidadForm


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


