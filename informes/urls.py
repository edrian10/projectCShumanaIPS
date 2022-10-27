from django.urls import path
from informes.models import HistoriaClinica 

urlpatterns = [
    path('',HistoriaClinica,name="historiaClinica"),
]