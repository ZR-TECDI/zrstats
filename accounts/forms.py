from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationFormConEmail(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # Pongo la primera letra del username en mayuscula
    # TODO limpiar caracteres raros (te miro a vos jager)
    def clean_username(self):
        nombre = self.cleaned_data['username']
        nombre = nombre.lower().capitalize()
        self.cleaned_data['username'] = nombre
        return nombre

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        # user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            user.miembro.email = self.cleaned_data["email"]
            user.save()
        return user

