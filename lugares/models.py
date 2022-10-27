from django.db import models
from django.forms import CharField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CiudadResidencia(models.Model):
    codigoCiudad=models.CharField(max_length=45, verbose_name="Codigo de Ciudad")
    nombre=models.CharField(max_length=45, verbose_name="Nombre de la ciudad")

class Localidad(models.Model):
    localidad=models.CharField(max_length=45, verbose_name="Localidad")
    nombreLocalidad=models.CharField(max_length=45, verbose_name="Nombres de la Localidad")
    ciudadResidencia=models.ForeignKey(CiudadResidencia, on_delete=models.CASCADE, verbose_name="Ciudad de residencia")
class EPS(models.Model):
    nombreEPS=models.CharField(max_length=45, verbose_name="Nombres de la EPS")
    class Estado(models.TextChoices):
        Activo='1',_('Activo')
        Inactivo='0',_('Inactivo')
    estado=models.CharField(max_length=2, choices=Estado.choices, default=Estado.Activo, verbose_name="Estado")
class Barrio(models.Model):
        barrio=models.CharField(max_length=45, verbose_name="Nombres del Barrio")
        codigoBarrio=models.CharField(max_length=45, verbose_name="Codigo del Barrio")
        localidad=models.ForeignKey(Localidad, on_delete=models.CASCADE, verbose_name="Localidad")