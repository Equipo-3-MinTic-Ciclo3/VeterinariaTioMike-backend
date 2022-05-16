from importlib import import_module
from django.contrib import admin

# Register your models here.
from .models.barrio import Barrio
from .models.departamento import Departamento
from .models.detalleFactura import DetalleFactura
from .models.proveedor import Proveedor
from .models.detalleMascota import DetalleMascota
from .models.ciudad import Ciudad
from .models.genero import Genero
from .models.factura import Factura

admin.site.register(Barrio)
admin.site.register(Departamento)
admin.site.register(DetalleFactura)
admin.site.register(Proveedor)