from django.urls import path
from informes.views import MenuP
from informes.views import ListarHc
from informes.views import HistoriaClinica
from informes.views import CrearH
from informes.views import BuscarH
from informes.views import ModificarH
from informes.views import ListarHc

urlpatterns = [
    path('menuP/',MenuP,name="menuP"),
    path('historiaClinica/',HistoriaClinica,name="historiaClinica"),
    path('crearH/',CrearH,name="crearH"),
    path('buscarH/',BuscarH,name="buscarH"),
    path('modificarH/',ModificarH,name="modificarH"),
    path('listarHc/',ListarHc,name="listarHc"),
]