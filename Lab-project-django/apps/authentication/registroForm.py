from django import forms

from django import forms
from apps.authentication.forms import SignUpForm
from apps.home.models import Estudiante
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(SignUpForm):

    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "nombre",
                "class": "form-control"}
        )
    )
    apellido = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "apellido",
                "class": "form-control"}
        )
    )
    programa_academico_id = forms.IntegerField()
