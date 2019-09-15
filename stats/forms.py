from django import forms
from .models import Clase, Rango, Nacionalidad, Rol, Unidad, Miembro, Mision, Asistencia


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


class MiembroForm(forms.ModelForm):
    class Meta:
        model = Miembro
        fields = ['email', 'nombre', 'peloton', 'escuadra', 'user', 'rango', 'clase1', 'unidad', 'rol']


class MisionForm(forms.ModelForm):
    class Meta:
        model = Mision
        fields = ['nombre', 'reporte', 'fecha', 'nombre_campa', 'editores', 'notas']


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['fecha', 'tiempo_de_sesion', 'requiere_atencion', 'mision', 'miembro']

