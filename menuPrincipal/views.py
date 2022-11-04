from multiprocessing import context
from django.shortcuts import render


# Create your views here.
def menuP(request):
    context={}
    return render(request,'menuPrincipal/menuP.html')