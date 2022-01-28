from django.contrib import admin

from app.app.models import Bodega, Producto_Bodega
from app.app.models import *
# Register your models here.

admin.site.register(Producto)
admin.site.register(Bodega)
admin.site.register(Producto_Bodega)