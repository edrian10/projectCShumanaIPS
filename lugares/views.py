from django.shortcuts import render,redirect
from lugares.forms import BarrioForm,BarrioUpdateForm
from lugares.forms import EPSForm,EPSUpdateForm
from lugares.models import Barrio
from lugares.models import EPS
from django.contrib import messages

# Create your views here.
def barrios(request, modal_status='hid'):
    titulo="Barrios"
    barrios= Barrio.objects.filter(estado='1')

    ### cuerpo del modal ###
    modal_title= ""
    modal_txt= ""
    modal_submit= ""
    ########################

    pk_barrio = ""
    tipo =None
    form_update= None
    form =BarrioForm()


    if request.method == "POST" and 'form-crear' in request.POST:
        form= BarrioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('barrios')
        else:
            form= BarrioForm(request.POST)
            messages.error(
                request,"Error al agregar la barrio"
            )
########################################## Configuracion Modal de eliminacion ###############################
    if request.method == "POST" and 'form-eliminar' in request.POST:
        modal_status= 'show'
        pk_barrio = request.POST['pk']
        barrio= Barrio.objects.get(id=pk_barrio)

        ## cuerpo del modal ##
        modal_title = f"Eliminar {barrio}"
        modal_txt= f"eliminar la barrio {barrio}"
        modal_submit="Eliminar"
        #######################

        tipo="eliminar"
########################################## Configuracion Modal de edición ###############################
    if request.method == "POST" and 'form-editar' in request.POST:
        modal_status= 'show'
        pk_barrio = request.POST['pk']
        barrio= Barrio.objects.get(id=pk_barrio)

        ## cuerpo del modal ##
        modal_title = f"Editar {barrio}"
        modal_submit="Editar"
        #######################

        tipo="editar"
        form_update= BarrioUpdateForm(instance=barrio)

########################################## Configuracion de eliminación ###############################
    if request.method == 'POST' and 'modal-confirmar' in request.POST:
        if request.POST['tipo'] == 'eliminar':
            barrio = Barrio.objects.filter(id = int(request.POST['modal-pk'])).update(
                estado='0'
            )
            messages.success(
                request,f"Se eliminó la barrio {barrio.nombre} exitosamente!"
            )
            return redirect('barrios')

        if request.POST['tipo'] == 'editar':
            pk_barrio = request.POST['modal-pk']
            barrio = Barrio.objects.get(id=pk_barrio)
            form_update=BarrioUpdateForm(request.POST, instance=barrio)

            if form_update.is_valid():
                form_update.save()
                messages.success(
                    request,f"Se editó la barrio {barrio.nombre} exitosamente!"
                )
                return redirect('barrios')
        
    context={
        'titulo':titulo,
        'barrios':barrios,
        'form':form,
        'modal_status':modal_status,
        'modal_submit': modal_submit,
        'modal_title': modal_submit,
        'modal_txt': modal_txt,
        'pk': pk_barrio,
        'tipo': tipo,
        'form_update':form_update

    }
    return render(request,'lugares/barrio.html',context)






# Create your views here EPS.
def eps(request, modal_status='hid'):
    titulo="EPS"
    eps= EPS.objects.filter(estado='1')

    ### cuerpo del modal ###
    modal_title= ""
    modal_txt= ""
    modal_submit= ""
    ########################

    pk_eps = ""
    tipo =None
    form_update= None
    form =EPSForm()


    if request.method == "POST" and 'form-crear' in request.POST:
        form= EPSForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eps')
        else:
            form= EPSForm(request.POST)
            messages.error(
                request,"Error al agregar la eps"
            )
########################################## Configuracion Modal de eliminacion ###############################
    if request.method == "POST" and 'form-eliminar' in request.POST:
        modal_status= 'show'
        pk_eps = request.POST['pk']
        eps= EPS.objects.get(id=pk_eps)

        ## cuerpo del modal ##
        modal_title = f"Eliminar {eps}"
        modal_txt= f"eliminar la eps {eps}"
        modal_submit="Eliminar"
        #######################

        tipo="eliminar"
########################################## Configuracion Modal de edición ###############################
    if request.method == "POST" and 'form-editar' in request.POST:
        modal_status= 'show'
        pk_eps = request.POST['pk']
        eps= EPS.objects.get(id=pk_eps)

        ## cuerpo del modal ##
        modal_title = f"Editar {eps}"
        modal_submit="Editar"
        #######################

        tipo="editar"
        form_update= EPSUpdateForm(instance=eps)

########################################## Configuracion de eliminación ###############################
    if request.method == 'POST' and 'modal-confirmar' in request.POST:
        if request.POST['tipo'] == 'eliminar':
            eps = EPS.objects.filter(id = int(request.POST['modal-pk'])).update(
                estado='0'
            )
            messages.success(
                request,f"Se eliminó la eps {eps.nombre} exitosamente!"
            )
            return redirect('eps')

        if request.POST['tipo'] == 'editar':
            pk_eps = request.POST['modal-pk']
            eps = EPS.objects.get(id=pk_eps)
            form_update=EPSUpdateForm(request.POST, instance=eps)

            if form_update.is_valid():
                form_update.save()
                messages.success(
                    request,f"Se editó la eps {eps.nombre} exitosamente!"
                )
                return redirect('eps')
        
    context={
        'titulo':titulo,
        'eps':eps,
        'form':form,
        'modal_status':modal_status,
        'modal_submit': modal_submit,
        'modal_title': modal_submit,
        'modal_txt': modal_txt,
        'pk': pk_eps,
        'tipo': tipo,
        'form_update':form_update

    }
    return render(request,'lugares/eps.html',context)