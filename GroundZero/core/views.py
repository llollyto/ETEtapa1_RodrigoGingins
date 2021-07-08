from django.http.response import HttpResponse
from django.shortcuts import  render,redirect
from .forms import ProveedorForm
from .models import Proveedor
from django.http.response import HttpResponse

# Create your views here.

def home(request):
    nombre= 'lolero lorerin'

    proveedores = Proveedor.objects.all()
   
    return render(request, 'home.html', context={'nom_usuario': nombre, 'datos': Proveedor}
    ) 
    
###INGRESAR###
def crearproveedor(request):
    data = {
        'form': ProveedorForm
    }  
    if request.method == 'POST':
        proveedor_form = ProveedorForm(data=request.POST)
        if proveedor_form.is_valid():
            proveedor_form.save()
            data["mensaje"] = "Proveedor guardado"
            return redirect('home')
        else:
            data["form"]= proveedor_form   
        return HttpResponse(request, 'core/form_crearproveedor.html', data)   
def Ingresar(request):
    data = {
        'form': ProveedorForm
    }
    if request.method == 'POST': 
        formulario = ProveedorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "xd"
            return redirect('index.html')
        else:
           data["form"]= formulario
    return render(request, 'core/form_crearproveedor.html', data)
###MOSTRAR####
def Ver(request):
    proveedores = Proveedor.objects.all()

    return render(request, 'core/ver.html', context={'proveedores':proveedores})


###MODIFICAR###
def form_mod_proveedor(request,idproveedor):
    proveedor = Proveedor.objects.get(idproveedor=idproveedor)

    datos ={
        'form': ProveedorForm(instance=proveedor)
    }
    if request.method == 'POST': 
        formulario = ProveedorForm(request.POST, instance = proveedor)
        if formulario.is_valid: 
            formulario.save()
            return redirect('ver')
    return render(request, 'core/form_mod_proveedor.html', datos)
    
 
###ELIMINAR###
def form_del_proveedor(request,idproveedor):
    proveedor = Proveedor.objects.get(idproveedor=idproveedor)
    proveedor.delete()
    return redirect('ver')