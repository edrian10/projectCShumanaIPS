from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def historiaClinica(request):
    context={}
    return render(request,'informes/historiaClinica.html')