from django import forms


class UploadReporteForm(forms.Form):
    file = forms.FileField()

