from multiprocessing import context
from django.shortcuts import render

def Usuarios(request):
    context={}
    return render(request,'usuarios/usuarios.html')

def Crear(request):
    context={}
    return render(request,'crear/crear.html')




