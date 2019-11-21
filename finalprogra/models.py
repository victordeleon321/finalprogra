from django.db import models
from django.contrib import admin
from django.utils import timezone
# Create your models here.

class Plato(models.Model):

    nombre  =   models.CharField(max_length=30)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre

class Empleado(models.Model):

    nombre  =   models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):

    nombre  =   models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Menu(models.Model):

    nombre    = models.CharField(max_length=60)
    total      = models.FloatField()
    platos   = models.ManyToManyField(Plato, through='Comida')


    def __str__(self):

        return self.nombre

class Comida (models.Model):

    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

class DetalleVenta (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

class ComidaInLine(admin.TabularInline):

    model = Comida
    extra = 1


class PlatoAdmin(admin.ModelAdmin):

    inlines = (ComidaInLine,)


class MenuAdmin (admin.ModelAdmin):

    inlines = (ComidaInLine,)
