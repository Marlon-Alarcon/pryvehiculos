from django.contrib import admin
from apps.vehiculos.models import Marca,TipoVehiculo,Vehiculo

# Register your models here.


class Vehiculoadmin(admin.ModelAdmin):
    list_display = ('modelo', 'color', 'placa', 'marca',"tipovehiculo")
    ordering = ('modelo', 'color', 'placa', 'marca','tipovehiculo')
    search_fields = ('modelo','marca__nombre', 'tipovehiculo__nombre')
    list_filter = ('modelo','marca__nombre', 'tipovehiculo__nombre')

admin.site.register(TipoVehiculo)
admin.site.register(Marca)
admin.site.register(Vehiculo, Vehiculoadmin)