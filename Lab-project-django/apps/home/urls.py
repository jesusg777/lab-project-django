# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from apps.home.views import MateriasListado, MateriaCrear, MateriaActualizar, MateriaDetalle, MateriaEliminar

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('landing/', views.home_page, name='landing_page'),

    path("selecUser/", views.user_select, name='user_select'),
   # path("horario/", views.ver_materia, name='ver_materia'),

    path("home_estudiante/", MateriasListado.as_view(template_name = "home/home_estudiante.html"), name='home_estudiante'),
    path("agregarMateria/", MateriaCrear.as_view(template_name = "home/agregar_materia.html"), name='agregar_materia'),
    path('detallesMateria/<int:pk>', MateriaDetalle.as_view(template_name = "home/materia_detalles.html"), name='detalles'),
    path('editarMateria/<int:pk>', MateriaActualizar.as_view(template_name = "home/actualizar_materia.html"), name='actualizar'),
    path("eliminarMateria/<int:pk>", MateriaEliminar.as_view(), name='eliminar_materia'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
