from django.db import models
from django.contrib import admin
from django.utils import timezone


class Usuario(models.Model):
    nombre = models.CharField(max_length=80)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.nombre

class Club(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    logo = models.CharField(max_length=255)
    usuarios = models.ManyToManyField(Usuario, through='MiembroClub')

    def __str__(self):
        return self.nombre

class MiembroClub (models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

class MiembroClubInLine(admin.TabularInline):
    model = MiembroClub
    extra = 1

class UsuarioAdmin(admin.ModelAdmin):
    inlines = (MiembroClubInLine,)

class ClubAdmin (admin.ModelAdmin):
    inlines = (MiembroClubInLine,)
