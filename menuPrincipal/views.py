from multiprocessing import context
from django.shortcuts import render


# Create your views here.
def MenuPrincipal(request):
    titulo="Menu Principal"
    context={
    'titulo':titulo
    }
    return render(request,'menuPrincipal/menuP.html')






