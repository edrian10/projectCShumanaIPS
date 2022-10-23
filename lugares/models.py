from django.db import models
from django.forms import CharField
from.utils.translation import gettext_lazy as _

# Create your models here.
class CiudadResidencia(models.model):
    codigoCiudad=models.CharField(_max_length=45, verbose_name="Codigo de Ciudad")
    nombre=models.CharField(_max_length=45, verbose_name="Nombre de la ciudad")

class Localidad(models.model):
    localidad=models.CharField(_max_length=45, verbose_name="Localidad")
    nombreLocalidad=models.CharField(_max_length=45, verbose_name="Nombres de la Localidad")
    ciudadResidencia=models.ForeignKey(CiudadResidencia, on_delete=models.CASCADE, verbose_name="Ciudad de residencia")
class EPS(models.model):
    nombreEPS=models.CharField(_max_length=45, verbose_name="Nombres de la EPS")
    class Estado(models.model):
        Activo='1',_('Activo')
        Inactivo='0',_('Inactivo')
    estado=models.CharField(max_length=2, choices=Estado.choices, default=Estado.Activo, verbose_name="Estado")
    class Barrio(models.model):
        barrio=models.CharField(_max_length=45, verbose_name="Nombres del Barrio")
        codigoBarrio=models.CharField(_max_length=45, verbose_name="Codigo del Barrio")
        localidad=models.ForeignKey(barrio, on_delete=models.CASCADE, verbose_name="Localidad")