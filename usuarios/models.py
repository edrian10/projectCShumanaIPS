from django.db import models
from django.forms import CharField
from django.utils.translation import gettext_lazy as _
from lugares.models import EPS, Barrio


#TABLA ESPECIALIDAD.
class Especialidad(models.Model):
    nombresEspecialidad=models.CharField(max_length=45, verbose_name="Nombres de la Especialidad")
    class Estado(models.TextChoices):
        Activo='1',_('Activo')
        Inactivo='0',_('Inactivo')
    estado=models.CharField(max_length=2, choices=Estado.choices, default=Estado.Activo, verbose_name="Estado")


#TABLA MEDICO
class Medico(models.Model):
    codigoMedico=models.CharField(max_length=45, verbose_name="Código de medico")
    class TipoDocumento(models.TextChoices):
        CC='CC', _('Cédula de Ciudadanía')
        TI='TI', _('Tarjeta de Identidad')
        RC='RC', _('Registro Civil')
        PP='PP', _('Pasaporte')
        CE='CE', _('Cédula de Extranjería')
        OT='OTRO',_('OT')
    tipoDocumento=models.CharField(max_length=6, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")
    numeroDocumento=models.CharField(max_length=50, verbose_name="Número de documento")
    nombres=models.CharField(max_length=45, verbose_name="Nombres")
    apellidos=models.CharField(max_length=45, verbose_name="Apellidos")
    telefono=models.CharField(max_length=20, verbose_name="Número de Teléfono")
    email=models.CharField(max_length=45, verbose_name="Email")
    cantServDia=models.CharField(max_length=45, verbose_name="Cantidad de servicios al día")
    cantServMes=models.CharField(max_length=45, verbose_name="Cantidad de servicios al Mes")
    class Estado(models.TextChoices):
        Activo='1',_('Activo')
        Inactivo='0',_('Inactivo')
    estado=models.CharField(max_length=2, choices=Estado.choices, default=Estado.Activo, verbose_name="Estado")
    especialidad=models.ForeignKey(Especialidad, on_delete=models.CASCADE, verbose_name="Especialidad")

#TABLA PACIENTES
class Pacientes(models.Model):
    nombres=models.CharField(max_length=45, verbose_name="Nombres")
    apellidos=models.CharField(max_length=45, verbose_name="Apellidos")
    edad=models.DateField(max_length=45, verbose_name="Edad")
    class TipoDocumento(models.TextChoices):
        CC='CC', _('Cédula de Ciudadanía')
        TI='TI', _('Tarjeta de Identidad')
        RC='RC', _('Registro Civil')
        PP='PP', _('Pasaporte')
        CE='CE', _('Cédula de Extranjería')
        OT='OTRO',_('OT')
    tipoDocumento=models.CharField(max_length=6, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")
    numeroDocumento=models.CharField(max_length=50, verbose_name="Número de documento")
    class Genero(models.TextChoices):
        F='F',_('Femenino')
        M='M',_('Masculino')
        OT='OTRO',_('OT')
    genero=models.CharField(max_length=4, choices=Genero.choices, default=Genero.OT, verbose_name="Genero")
    class GrupoSanguineo(models.TextChoices):
        A_POSITIVO ='A+', _('A+')
        A_NEGATIVO='A-', _('A-')
        B_POSITIVO='B+', _('B+')
        B_NEGATIVO='B-', _('B-')
        AB_POSITIVO='AB+', _('AB+')
        AB_NEGATIVO='AB-', _('AB-')
        O_POSITIVO='O+', _('O+')
        O_NEGATIVO='O-',_('O-')
    grupoSanguineo=models.CharField(max_length=20, choices=GrupoSanguineo.choices, verbose_name="Grupo Sanguineo")
    direccion=models.CharField(max_length=45, verbose_name="Dirección")
    email=models.CharField(max_length=45, verbose_name="Email")
    telefono=models.CharField(max_length=20, verbose_name="Número de Teléfono")
    class EstadoCivil(models.TextChoices):
        Casado ='Casado', _('Casado')
        Divorciado ='Divorciado', _('Divorciado')
        Soltero ='Soltero', _('Soltero')
        Separado='Separado',_('Separado')
        Otro ='OTRO', _('OT')
    estadoCivil=models.CharField(max_length=10, choices=EstadoCivil.choices, default=EstadoCivil.Otro, verbose_name="Estado Civil")
    ocupacion=models.CharField(max_length=100, verbose_name="Ocupación")
    class RegimenSalud(models.TextChoices):
        subsidiado='subsidiado',_('subsidiado')
        contributivo='contributivo',_('contributivo')
        OT='OTRO', _('OT')
    genero=models.CharField(max_length=4, choices=Genero.choices, default=Genero.OT, verbose_name="Genero")
    class Estado(models.TextChoices):
        Activo='1',_('Activo')
        Inactivo='0',_('Inactivo')
    estado=models.CharField(max_length=2, choices=Estado.choices, default=Estado.Activo, verbose_name="Estado")
    eps=models.ForeignKey(EPS, on_delete=models.CASCADE, verbose_name="Paciente")
    barrio=models.ForeignKey(Barrio, on_delete=models.CASCADE, verbose_name="Barrio")

#TABLA USUARIOS
class Usuarios(models.Model):
    nombres=models.CharField(max_length=45, verbose_name="Nombres")
    apellidos=models.CharField(max_length=45, verbose_name="Apellidos")
    class TipoDocumento(models.TextChoices):
        CC='CC', _('Cédula de Ciudadanía')
        TI='TI', _('Tarjeta de Identidad')
        RC='RC', _('Registro Civil')
        PP='PP', _('Pasaporte')
        CE='CE', _('Cédula de Extranjería')
        OT='OTRO',('OT')
    tipoDocumento=models.CharField(max_length=45, choices=TipoDocumento.choices, verbose_name="Tipo de Documento")
    numeroDocumento=models.CharField(max_length=50, verbose_name="Número de documento")
    telefono=models.CharField(max_length=45, verbose_name="Número de Teléfono")
    email=models.CharField(max_length=45, verbose_name="email")
    class TipoUsuario(models.TextChoices):
        Administrador ='Administrador', _('Administrador')
        Recepcionista='Recepcionista', _('Recepcionista')
    tipoUsuario=models.CharField(max_length=13, choices=TipoUsuario.choices, default=TipoUsuario.Recepcionista, verbose_name="Tipo de Usuario")
    class Estado(models.TextChoices):
        Activo='1',_('Activo')
        Inactivo='0',_('Inactivo')
    estado=models.CharField(max_length=2, choices=Estado.choices, default=Estado.Activo, verbose_name="Estado")
    
