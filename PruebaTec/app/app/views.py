
from django.shortcuts import redirect, render
from .models import Bodega, Producto, Producto_Bodega
from django.contrib import messages
from django.views.generic import CreateView
from .forms import ProductoBodegaForm

# Create your views here.

def home(request):
    return render(request, "index.html")

def productos(request):
    productosListados = Producto.objects.all() 
    return render(request, "producto.html", {"productos": productosListados})

def bodegas(request):
    bodegasListado = Bodega.objects.all()
    return render(request, "bodega.html", {"bodegas" : bodegasListado})   

def stock(request):
    stockProductos = Producto_Bodega.objects.all()
    return render(request, "stock.html", {"stockProductos": stockProductos})      


def ingresarProducto(request):
    
    nombre = request.POST['txtNombreProducto']
    descripcion = request.POST['txtDescripcionProducto']
    producto = Producto.objects.create(nombre=nombre, descripcion=descripcion)
    messages.success(request, '¡Producto Registrado!')
    return redirect('productos')

def eliminarProducto(request, id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    messages.success(request, '¡Producto Eliminado!')
    return redirect('productos')
    
def edicionProducto(request, id):
    producto = Producto.objects.get(id = id)
    return render(request, "edicion_producto.html", {"producto" : producto})

def editarProducto(request):
    id  = request.POST['txtIdProducto']
    nombre = request.POST['txtNombreProducto']
    descripcion = request.POST['txtDescripcionProducto']
    activo = request.POST['checkProductoActivo']

    producto = Producto.objects.get(id = id)
    producto.id = id
    producto.nombre = nombre
    producto.descripcion = descripcion
    producto.activo = activo

    producto.save()
    return redirect('productos')
     

def ingresarBodega(request):
    nombreB = request.POST['txtNombreBodega']
    ubicacion = request.POST['txtUbicacion']
    bodega = Bodega.objects.create(nombre=nombreB, ubicacion=ubicacion)
    messages.success(request,'¡Bodega Registrada!')     
    return redirect('bodegas')
    
def eliminarBodega(request, id):
    bodega = Bodega.objects.get(id = id)
    bodega.delete()
    messages.success(request, '¡Bodega Eliminada!')
    return redirect('bodegas')

def edicionBodega(request, id):
    bodega = Bodega.objects.get(id = id)
    return render(request, "edicion_bodega.html", {"bodega" : bodega})  

def editarBodega(request):
    id = request.POST['txtIdBodega']
    nombre = request.POST['txtNombreBodega']
    ubicacion = request.POST['txtUbicacion']
   
    bodega = Bodega.objects.get(id = id)
    
    bodega.nombre = nombre
    bodega.ubicacion = ubicacion
    
    bodega.save()
    return redirect('bodegas')    



def ingresarStock(request):
    if request.method == 'POST':
        form = ProductoBodegaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('stock')
    else:
        form = ProductoBodegaForm()
    return render(request, 'ingresar_stock.html', {'form': form})            