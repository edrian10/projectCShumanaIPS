from django.urls import path
from menuPrincipal.views import menuP 


urlpatterns = [
    path('menuP/',menuP,name="menuP"),
]