from django.urls import path

from usuarios.models import Pacientes
from usuarios.views import usuario,usuarios_crear,usuarios_modificar,usuarios_eliminar,usuarios_listar
from usuarios.views import medico,medicos_crear,medicos_modificar,medicos_eliminar,medicos_listar
from usuarios.views import paciente,pacientes_crear,pacientes_modificar,pacientes_eliminar,pacientes_listar

urlpatterns = [
    path('',usuario,name="usuarios"),
    path('crear/',usuarios_crear,name="u-crear"),
    path('modificar/',usuarios_modificar,name="u-modificar"),
    path('eliminar/',usuarios_eliminar,name="u-eliminar"),
    path('listar/',usuarios_listar,name="u-listar"),

    path('pacientes/',paciente,name="pacientes"),
    path('pacientes/crear/',pacientes_crear,name="p-crear"),
    path('pacientes/modificar/',pacientes_modificar,name="p-modificar"),
    path('pacientes/eliminar/',pacientes_eliminar,name="p-eliminar"),
    path('listar/',pacientes_listar,name="p-listar"),

    path('medicos/',medico,name="medicos"),
    path('medicos/crear/',medicos_crear,name="m-crear"),
    path('medicos/modificar/',medicos_modificar,name="m-modificar"),
    path('medicos/eliminar/',medicos_eliminar,name="m-eliminar"),
    path('listar/',medicos_listar,name="m-listar"),
] 
