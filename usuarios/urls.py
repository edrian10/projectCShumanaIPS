from django.urls import path
from menuPrincipal.views import Usuarios
from usuarios.views import Crear

urlpatterns = [
    path('usuarios',Usuarios,name="usuarios"),
    path('crear',Crear,name="crear"),
]

