from cProfile import label
from dataclasses import fields
from django.forms import ModelForm, widgets
from .models import *
from django import forms

class ProductoBodegaForm(ModelForm):
    class Meta:
        model = Producto_Bodega
        fields = [
            'producto_id', 
            'bodega_id', 
            'stock',
        ]
        labels ={
            
            'producto_id': 'Producto', 
            'bodega_id':'Bodega', 
            'stock': 'Stock',
        }
        widgets = { 
            'producto_id': forms.Select(attrs={'class':'form-control'}),
            'bodega_id':forms.Select(attrs={'class':'form-control'}),
            'stock': forms.NumberInput(attrs={'class':'form-control'})
        }

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class BodegaForm(ModelForm):
    class Meta:
        model = Bodega
        fields = '__all__'
         