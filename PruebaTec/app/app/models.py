
from csv import excel_tab
from django.db import models
import uuid
from django.core.exceptions import ValidationError


# Create your models here.

# Modelo Producto
class Producto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(verbose_name="Ingrese descripcion", null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        txt = " {0} / {1}"
        if(self.activo):
            act = "Activo"
        else:
            act = "Inhabilitado"    
        return txt.format(self.nombre, act)

         
# Modelo Bodega
class Bodega(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50, unique=True)
    ubicacion = models.CharField(max_length=200)
    
    def __str__(self):
        txt = " {0} "
        return txt.format(self.nombre)

# Modelo Producto_bodega --> La funcion de este modelo es el ingreso de estock de un producto en una bodega seleccionada
class Producto_Bodega(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    producto_id = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
    bodega_id = models.ForeignKey(Bodega, null=False, blank=False, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0, null=False, blank=False)


    def __str__(self):
        txt = "Producto: {0} / Bodega: {1} / Stock: {2}"
        return txt.format(self.producto_id.nombre, self.bodega_id.nombre, self.stock  )
        
    