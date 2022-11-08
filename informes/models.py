from django.db import models
from usuarios2.models import Medico, Pacientes

# Create your models here
# TABLA DE HISTORIA CLÍNICA.
class HistoriaClinica(models.Model):
    fechaAtencion=models.DateField(max_length=20, verbose_name="Fecha de Atención")
    motivoConsulta=models.CharField(max_length=45, verbose_name="Motivo de la Consulta")
    causasExternas=models.CharField(max_length=45, verbose_name="Causas Externas")
    alergiaMedicamento=models.CharField(max_length=245, verbose_name="Alergia a Medicamento")
    cirugiasRecibidas=models.CharField(max_length=245, verbose_name="Cirugias recibidas")
    tratamientosMedicamentos=models.CharField(max_length=245, verbose_name="Tratamiento o Medicamentos")
    informeYtratamientos=models.CharField(max_length=245, verbose_name="Informe Medico y tratamientos")
    nombresAcompañante=models.CharField(max_length=45, verbose_name="Nombres del Acompañante")
    telAcompañante=models.CharField(max_length=45, verbose_name="Teléfono del Acompañante")
    pacientes=models.ForeignKey(Pacientes, on_delete=models.CASCADE, verbose_name="Paciente")
    medico=models.ForeignKey(Medico, on_delete=models.CASCADE, verbose_name="Medico")