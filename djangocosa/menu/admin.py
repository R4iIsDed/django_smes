from django.contrib import admin

from .models import Region, Comuna, Rol, Pregunta, Usuario, Direccion, Categoria, Producto, Factura, Detalle 
# Register your models here.

admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Rol)
admin.site.register(Pregunta)
admin.site.register(Usuario) 
admin.site.register(Direccion)
admin.site.register(Categoria)
admin.site.register(Factura)
admin.site.register(Detalle)
admin.site.register(Producto)
