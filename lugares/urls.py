from django.urls import path
from lugares.views import barrios,eps

urlpatterns = [
    path('barrios/',barrios,name='barrios'),
    path('barrios/<str:modal_status>/',barrios,name='barrios'),
    
    path('eps/',eps,name='eps'),
    path('eps/<str:modal_status>/',eps,name='eps'),
]
