from importlib.resources import path
from unicodedata import name
from django.urls import path
from . import views


urlpatterns =[
    path('productos/', views.productos, name='productos'),
    path('stock/',views.stock, name='stock'),
    path('ingresarStock/', views.ingresarStock, name='ingresar-stock' ),
    path('ingresarProducto/', views.ingresarProducto, name='ingresar-producto'),
    path('productos/eliminarProducto/<id>', views.eliminarProducto, name='eliminar-producto'),
    path('productos/edicionProducto/<id>', views.edicionProducto),
    path('editarProducto/', views.editarProducto, name='editar-producto'),
    path('bodegas/',views.bodegas, name='bodegas'),
    path('ingresarBodegas/', views.ingresarBodega, name='ingresar-bodega'),
    path('bodegas/edicionBodega/<id>', views.edicionBodega),
    path('editarBodega/', views.editarBodega, name='editar-bodega'),
    path('bodegas/eliminarBodega/<id>', views.eliminarBodega, name='eliminar-bodega'),
    
]
 