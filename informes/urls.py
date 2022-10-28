from django.urls import path
from informes.views import historiaClinica 

urlpatterns = [
    path('historia/',historiaClinica,name="historiaClinica"),
]