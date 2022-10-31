from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def HistoriaClinica(request):
    context={}
    return render(request,'informes/historiaClinica.html')

def CrearH(request):
    context={}
    return render(request,'informes/crearH.html')

def BuscarH(request):
    context={}
    return render(request,'informes/buscarH.html')

def ModificarH(request):
    context={}
    return render(request,'informes/modificarH.html')
    
def ListarHc(request):
    context={}
    return render(request,'informes/listarHc.html')

def MenuP(request):
    context={}
    return render(request,'informes/menuP.html')