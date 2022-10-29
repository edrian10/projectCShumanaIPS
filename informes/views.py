from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def MenuP(request):
    context={}
    return render(request,'informes/menuP.html')

def HistoriaClinica(request):
    context={}
    return render(request,'informes/historiaClinica.html')

def CrearH(request):
    context={}
    return render(request,'informes/crearH.html')

def BuscarH(request):
    context={}
    return render(request,'informes/buscarH.html')