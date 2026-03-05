# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from apps.authentication.registroForm import RegistroForm
from apps.home.models import Estudiante
from .forms import LoginForm, SignUpForm


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/home_estudiante/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = RegistroForm(request.POST)

        if form.is_valid():
            # Guardar usuario
            usuario = form.save()
            print("sdafsagasdfgnsdfkljgbhnaierlugnbhaksjdhnbfglkadsfjhngbaksdjbf")
            # Guardar estudiante
            estudiante = Estudiante.objects.create(
                codigo=form.cleaned_data['username'],
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                contrasena = form.cleaned_data['password1'],
                correo = form.cleaned_data['email'],
                programa_academico_id=form.cleaned_data['programa_academico_id'],
                # Otros campos del estudiante
            )

            return redirect("/login/")

        else:
            msg = 'Form is not valid'
            
    else:
        form = RegistroForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
