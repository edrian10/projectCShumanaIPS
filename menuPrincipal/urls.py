from django.urls import path
from menuPrincipal.views import MenuPrincipal



urlpatterns = [
    path('',MenuPrincipal,name="menuP"),
]