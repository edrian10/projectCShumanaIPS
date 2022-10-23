from django.db import models

# Create your models here.
class Usuarios(models.model):
    nombres=models.CharField(_max_length=45, verbose_name="Nombres")
    apellidos=models.CharField(_max_length=45, verbose_name="Apellidos")
    class TipoDocumento(models.model):
        CC='CC', _('Cédula de Ciudadania')
        TI='TI', _('Tarjeta de Identidad')
        RC='RC', _('Registro Civil')
        PP='PP', _('Pasaporte')
        CE='CE', _('Cédula de Extranjeria')
        OT='Otros_('Otro Tipo de Identidad')
    tipoDocumento=models,CharField(max_length=4, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")
    numeroDocumento=models.CharField(max_length=50, verbose_name="Número de documento")
    telefono=models.CharField(max_length=20, verbose_name="Número de Telefono")
    email=models.CharField(max_length=100, verbose_name="email")
    class Genero(models.model):
        F='F', _('Cédula de Ciudadania')
        TI='TI', _('Tarjeta de Identidad')
        RC='RC', _('Registro Civil')
        PP='PP', _('Pasaporte')
        CE='CE', _('Cédula de Extranjeria')
        OT='Otros_('Otro Tipo de Identidad')
   genero=models,CharField(max_length=4, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")