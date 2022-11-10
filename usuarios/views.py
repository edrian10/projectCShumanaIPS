from multiprocessing import context
from django.shortcuts import render

def Usuarios(request):
    context={}
    return render(request,'usuarios/usuarios.html')

def CrearUs(request):
    context={}
    return render(request,'usuarios/crearUs.html')

def Modificar(request):
    context={}
    return render(request,'usuarios/modificar.html')

def Buscar(request):
    context={}
    return render(request,'usuarios/buscar.html')

def Listar(request):
    context={}
    return render(request,'usuarios/listar.html')

def Pacientes(request):
    context={}
    return render(request,'pacientes/pacientes.html')


