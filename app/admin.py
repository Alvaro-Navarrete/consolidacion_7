from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'pais', 'ciudad']
    search_fields = ['id', 'nombre']
    
@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'laboratorio', 'especialidad']
    search_fields = ['id', 'nombre']
    

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta',]
    search_fields = ['id', 'nombre']