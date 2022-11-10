from django.urls import path


from usuarios.views import Buscar, CrearUs, Listar, Modificar, Pacientes,Usuarios

urlpatterns = [
    path('',Usuarios,name="usuarios"),
    path('crearUs/',CrearUs,name="crearUs"),
    path('buscar/',Buscar,name="buscar"),
    path('listar/',Listar,name="listar"),
    path('modificar/',Modificar,name="modificar"),
    path('crearUs/',CrearUs,name="crearUs"),
    path('pacientes/',Pacientes,name="pacientes"),
]
