# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Profesor(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    facultad = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Programa(models.Model):
    nombre = models.CharField(max_length=100)

class Semestre(models.Model):
    codigo = models.IntegerField(primary_key=True)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name="semestres")
    numeroSemestre = models.IntegerField()
    cantidadCreditos = models.IntegerField()

    def __str__(self):
        return str(self.numeroSemestre)

class Materia(models.Model):
    codigoMateria = models.IntegerField(primary_key=True)
    nombreMateria = models.CharField(max_length=100) 
    profesorAsignado = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='materias')
    cantCreditos = models.IntegerField()
    horario = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    puntuacion = models.CharField(max_length=100)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE, related_name='materias')

class Estudiante(models.Model):

    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    programa_academico = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name='estudiantes')
    materias = models.ManyToManyField(Materia, through='Inscripcion', related_name='estudiantes')
    contrasena = models.CharField(max_length=20)


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    aprobado = models.BooleanField(default=False)
    cursando = models.BooleanField()

class Valoracion(models.Model):
    asunto = models.CharField(max_length=100)
    comentario = models.CharField(max_length=100)
    puntuacion = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='valoraciones')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='valoraciones')
