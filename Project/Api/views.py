from django.shortcuts import render,get_object_or_404
from .forms import *
# Create your views here.
from django.db.models import Q
# ---> No exijas la validación CSRF para esta vista (html)
# from django.views.decorators.csrf import csrf_exempt

#--> Importación de Libreria de Permisos de Usuarios
from django.contrib.auth.decorators import login_required, permission_required



def Home(request):
    query=Producto.objects.all()
    data={
        'formulario':query
    }
    return render(request, 'Base.html',data)

@permission_required('Api.view_producto', login_url='home')
def Productos(request):
    query=Producto.objects.all()
    Filtro= request.GET.get('Filtrar')
    if Filtro:
        query= Producto.objects.filter(
            Q(Nombre__icontains=Filtro)
        ).distinct()
    data={
        'ListarProductos':query
    }
    return render(request, 'Pages/VerProductos.html',data)


#---> Obligamos a Loguearse para realizar el CRUD
@login_required
# --> no necesita comprobar el token CSRF
# @csrf_exempt
@permission_required('Api.add_producto', login_url='home')
def NuevoProductos(request):
    data={
        'Formulario': FormularioProductos()
    }
    if request.method == 'POST':
        formulario = FormularioProductos(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['Mensaje'] = "Producto Guardado Correctamente"
        else:
            data['Mensaje'] = "Error al Guardar el Producto"
    return render(request, 'Pages/NuevoProducto.html', data)


@permission_required('Api.change_producto', login_url='Home')

def ModificarProductos(request,Codigo):
    buscar=get_object_or_404(Producto, Codigo=Codigo)
    data={
        'Formulario': FormularioProductos(instance=buscar)
    }
    if request.method == 'POST':
        formulario = FormularioProductos(data=request.POST,instance=buscar,files=request.FILES)
        
        if formulario.is_valid():
            formulario.save()
            data['Mensaje'] = "Producto Modificados Correctamente"
        else:
            data['Mensaje'] = "Error al Actualizar el Producto"
    return render(request, 'Pages/ModificarProducto.html', data)


