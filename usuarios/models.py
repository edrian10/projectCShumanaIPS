
from django.db import models
from django.forms import CharField

from informes.models import Informe
from.utils.translation import gettext_lazy as _

#TABLA ESPECIALIDAD.
class Especialidad(models.model):
    nombresEspecialidad=models.CharField(_max_length=45, verbose_name="Nombres de la Especialidad")
    class Estado(models.model):
        Activo='1',_('Activo')
        Inactivo='0',_('Inactivo')
    estado=models.CharField(max_length=2, choices=Estado.choices, default=Estado.Activo, verbose_name="Estado")


#TABLA MEDICO
class Medico(models.model):
    codigoMedico=models.CharField(_max_length=45, verbose_name="Código de medico")
    class TipoDocumento(models.model):
        CC='CC', _('Cédula de Ciudadanía')
        TI='TI', _('Tarjeta de Identidad')
        RC='RC', _('Registro Civil')
        PP='PP', _('Pasaporte')
        CE='CE', _('Cédula de Extranjería')
        OT='Otros',_('Otro Tipo de Identidad')
    tipoDocumento=models,CharField(max_length=6, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")
    numeroDocumento=models.CharField(max_length=50, verbose_name="Número de documento")
    nombres=models.CharField(_max_length=45, verbose_name="Nombres")
    apellidos=models.CharField(_max_length=45, verbose_name="Apellidos")
    telefono=models.CharField(max_length=20, verbose_name="Número de Teléfono")
    email=models.CharField(max_length=45, verbose_name="Email")
    cantServDia=models.CharField(_max_length=45, verbose_name="Cantidad de servicios al día")
    cantServMes=models.CharField(_max_length=45, verbose_name="Cantidad de servicios al Mes")
    class Estado(models.model):
        Activo='1',_('Activo')
        Inactivo='0',_('Inactivo')
    estado=models.CharField(max_length=2, choices=Estado.choices, default=Estado.Activo, verbose_name="Estado")
    Usuarios=models.ForeignKey(Usuarios, on_delete=models.CASCADE, verbose_name="Usuarios")
    Especialidad=models.ForeignKey(Especialidad, on_delete=models.CASCADE, verbose_name="Especialidad")

#TABLA PACIENTES
class Pacientes(models.model):
    nombres=models.CharField(_max_length=45, verbose_name="Nombres")
    apellidos=models.CharField(_max_length=45, verbose_name="Apellidos")
    edad=models.DateField(_max_length=45, verbose_name="Edad")
    class TipoDocumento(models.model):
        CC='CC', _('Cédula de Ciudadanía')
        TI='TI', _('Tarjeta de Identidad')
        RC='RC', _('Registro Civil')
        PP='PP', _('Pasaporte')
        CE='CE', _('Cédula de Extranjería')
        OT='Otros',_('Otro Tipo de Identidad')
    tipoDocumento=models,CharField(max_length=6, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")
    numeroDocumento=models.CharField(max_length=50, verbose_name="Número de documento")
    class Genero(models.model):
        F='F',_('Femenino')
        M='M',_('Masculino')
        OT='OTRO',_('Otro')
    genero=models.CharField(max_length=4, choices=Genero.choices, default=Genero.OTROS, verbose_name="Genero")
    class GrupoSanguineo(models.model):
        A_POSITIVO ='A+', _('A+')
        A_NEGATIVO='A-', _('A-')
        B_POSITIVO='B+', _('B+')
        B_NEGATIVO='B-', _('B-')
        AB_POSITIVO='AB+', _('AB+')
        AB_NEGATIVO='AB+', _('AB-')
        O_POSITIVO='O+', _('O+')
        O_NEGATIVO='O-',_('O-')
    grupoSanguineo=models,CharField(max_length=20, choices=GrupoSanguineo.choices, default=GrupoSanguineo.CC, verbose_name="Grupo Sanguineo")
    direccion=models.CharField(max_length=45, verbose_name="Dirección")
    email=models.CharField(max_length=45, verbose_name="Email")
    telefono=models.CharField(max_length=20, verbose_name="Número de Teléfono")
    class EstadoCivil(models.model):
        Casado ='Casado', _('Casado')
        Divorciado ='Divorciado', _('Divorciado')
        Soltero ='Soltero', _('Soltero')
        Separado='Separado',_('Separado')
        Otro ='Otro', _('Otro')
    estadoCivil=models,CharField(max_length=10, choices=EstadoCivil.choices, default=EstadoCivil.Otro, verbose_name="Estado Civil")
    ocupacion=models.CharField(_max_length=100, verbose_name="Ocupación")
    class RegimenSalud(models.model):
        subsidiado='subsidiado',_('subsidiado')
        contributivo='contributivo',_('contributivo')
        OT='OTRO', _('Otro')
    genero=models.CharField(max_length=4, choices=Genero.choices, default=Genero.OTRO, verbose_name="Genero")
    class Estado(models.model):
        Activo='1',_('Activo')
        Inactivo='0',_('Inactivo')
    estado=models.CharField(max_length=2, choices=Estado.choices, default=Estado.Activo, verbose_name="Estado")
    EPS=models.ForeignKey(EPS, on_delete=models.CASCADE, verbose_name="Paciente")
    barrio=models.ForeignKey(Barrio, on_delete=models.CASCADE, verbose_name="Barrio")
    #Falta configurar las llaves foráneas de eps y barrio no se si van en este usuarios.


#TABLA USUARIOS

class Usuarios(models.model):
    nombres=models.CharField(_max_length=45, verbose_name="Nombres")
    apellidos=models.CharField(_max_length=45, verbose_name="Apellidos")
    class TipoDocumento(models.model):
        CC='CC', _('Cédula de Ciudadanía')
        TI='TI', _('Tarjeta de Identidad')
        RC='RC', _('Registro Civil')
        PP='PP', _('Pasaporte')
        CE='CE', _('Cédula de Extranjería')
        OT='Otros',('Otro Tipo de Identidad')
    tipoDocumento=models,CharField(max_length=6, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")
    numeroDocumento=models.CharField(max_length=50, verbose_name="Número de documento")
    telefono=models.CharField(max_length=20, verbose_name="Número de Teléfono")
    email=models.CharField(max_length=100, verbose_name="email")
    class TipoUsuario(models.model):
        Administrador ='Administrador', _('Administrador')
        Recepcionista='Recepcionista', _('Recepcionista')
    tipoUsuario=models.CharField(max_length=4, choices=TipoUsuario.choices, default=TipoUsuario.OTROS, verbose_name="Tipo de Usuario")
    class Estado(models.model):
        Activo='1',_('Activo')
        Inactivo='0',_('Inactivo')
    estado=models.CharField(max_length=2, choices=Estado.choices, defaulT=Estado.Activo, verbose_name="Estado")
    pacientes=models.ForeignKey(Pacientes, on_delete=models.CASCADE, verbose_name="Paciente")

        #LA LLAVE FORÁNEA DE INFORMES PERTENECE A OTRO GRUPO NO SE DONDE DEBO HACER LA TABLA
    informes=models.ForeignKey(Informe, on_delete=models.CASCADE, verbose_name="informes")

