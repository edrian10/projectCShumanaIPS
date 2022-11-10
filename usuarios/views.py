
from django.shortcuts import render

def usuario(request):
    context={}
    return render(request,'usuarios/usuarios.html', context)

def usuarios_crear(request):
    context={}
    return render(request,'usuarios/crear.html', context)

def usuarios_listar(request):
    context={}
    return render(request,'usuarios/listar.html', context)


def usuarios_modificar(request):
    context={}
    return render(request,'usuarios/u-modificar.html', context)

def usuarios_eliminar(request):
    context={}
    return render(request,'usuarios/usuarios.html', context)


def medico(request):
    context={}
    return render(request,'usuarios/medicos/medicos.html', context)

def medicos_crear(request):
    context={}
    return render(request,'usuarios/medicos/m-crear.html', context)

def medicos_listar(request):
    context={}
    return render(request,'usuarios/medicos/listar.html', context)

def medicos_modificar(request):
    context={}
    return render(request,'usuarios/medicos/m-modificar.html', context)

def medicos_eliminar(request):
    context={}
    return render(request,'usuarios/medicos/medicos.html', context)


def paciente(request):
    context={}
    return render(request,'usuarios/pacientes/pacientes.html', context)

def pacientes_crear(request):
    context={}
    return render(request,'usuarios/pacientes/crear.html', context)

def pacientes_listar(request):
    context={}
    return render(request,'usuarios/pacientes/listar.html', context)


def pacientes_modificar(request):
    context={}
    return render(request,'usuarios/pacientes/p-modificar.html', context)

def pacientes_eliminar(request):
    context={}
    return render(request,'usuarios/pacientes/pacientes.html', context)

