from django.shortcuts import render, redirect

def inicio(request):
    context={}
    return render(request,'index.html', context)


