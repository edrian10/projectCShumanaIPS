from django.db import models

from usuarios.models import Medico, Pacientes

# Create your models here
# TABLA DE HISTORIA CLÍNICA.
class HistoriaClinica(models.model):
    fechaAtencion=models.DateField(_max_length=20, verbose_name="Fecha de Atención")
    motivoConsulta=models.CharField(_max_length=45, verbose_name="Motivo de la Consulta")
    causasExternas=models.CharField(_max_length=45, verbose_name="Causas Externas")
    alergiaMedicamento=models.CharField(_max_length=245, verbose_name="Alergia a Medicamento")
    cirugiasRecibidas=models.CharField(_max_length=245, verbose_name="Cirugias recibidas")
    tratamientosMedicamentos=models.CharField(_max_length=245, verbose_name="Tratamiento o Medicamentos")
    informeYtratamientos=models.CharField(_max_length=245, verbose_name="Informe Medico y tratamientos")
    nombresAcompañante=models.CharField(_max_length=45, verbose_name="Nombres del Acompañante")
    telAcompañante=models.CharField(_max_length=45, verbose_name="Teléfono del Acompañante")
    pacientes=models.ForeignKey(Pacientes, on_delete=models.CASCADE, verbose_name="Paciente")
    medico=models.ForeignKey(Medico, on_delete=models.CASCADE, verbose_name="Medico")

class Informe(models.model):
    cantidadDeServiosDia=models.CharField(_max_length=20, verbose_name="Fecha de Atención")
    fechaGeneracionInforme=models.DateField(_max_length=20, verbose_name="Fecha de Atención")
    fechaInicioInforme=models.DateField(_max_length=20, verbose_name="Fecha de Atención")
    fechaFinInforme=models.DateField(_max_length=20, verbose_name="Fecha de Atención")

# TABLA DE DETALLE INFORME.
class DetalleInforme(models.model):
    informe=models.ForeignKey(Informe, on_delete=models.CASCADE, verbose_name="Informe")
    historiaClinica=models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE, verbose_name="Historia Clínica")
    