from django import forms
from .models import Clase, Rango, Nacionalidad, Rol, Unidad, Miembro, Mision, Asistencia, Campana
from django_select2.forms import HeavySelect2MultipleWidget, HeavySelect2Widget, ModelSelect2MultipleWidget, \
    ModelSelect2TagWidget, ModelSelect2Widget, Select2MultipleWidget, Select2Widget


class MisionForm(forms.ModelForm):
    class Meta:
        model = Mision
        fields = ['nombre', 'oficial', 'tipo', 'estado', 'campana', 'descripcion',
                  'notas_privadas', 'notas_editor', 'imagen', 'briefing', 'mapa', 'fecha_programada',
                  'reporte', 'autor', 'editores', 'responsables']
        widgets = {
            'autor': Select2Widget,
            'campana': Select2Widget,
            'editores': Select2MultipleWidget,
            'responsables': Select2MultipleWidget,
        }


class MisionReporteForm(forms.ModelForm):
    class Meta:
        model = Mision
        fields = ['reporte']


class UploadReporteForm(forms.Form):
    file = forms.FileField()


class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = ['clase', 'abreviatura']


class RangoForm(forms.ModelForm):
    class Meta:
        model = Rango
        fields = ['rango', 'abreviatura', 'orden']


class NacionalidadForm(forms.ModelForm):
    class Meta:
        model = Nacionalidad
        fields = ['pais', 'abreviatura']


class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['rol', 'abreviatura']


class UnidadForm(forms.ModelForm):
    class Meta:
        model = Unidad
        fields = ['nombre', 'abreviatura']


class CampanaForm(forms.ModelForm):
    class Meta:
        model = Campana
        fields = ['nombre', 'tipo', 'descripcion', 'estado']


class MiembroForm(forms.ModelForm):
    class Meta:
        model = Miembro
        fields = ['email', 'nombre', 'peloton', 'escuadra', 'avatar', 'user', 'rango', 'clase1', 'unidad', 'rol']


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['fecha', 'tiempo_de_sesion', 'requiere_atencion', 'mision', 'miembro']

