from django.urls import path
from lugares.views import barrios

urlpatterns = [
    path('barrios/',barrios,name='barrios'),
    path('barrios/<str:modal_status>/',barrios,name='barrios'),
]
