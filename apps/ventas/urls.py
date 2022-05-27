from django.urls import path
from apps.ventas.views import listVentas, ventaCreate, ventaEdit, ventaElim, listVehiculoventa, VehiculoventaCreate, VehiculoventaEdit, VehiculoventaElim, consulta1, consulta2, consulta3, consulta4

app_name='ventas'
urlpatterns = [
    path('', listVentas, name='listVentas'),
    path('nuevo/', ventaCreate, name='ventaCreate'),
    path('actualizar/<int:id_venta>/', ventaEdit, name='ventaEdit'),
    path('eliminar/<int:id_venta>/', ventaElim, name='ventaElim'),

    #Venta Vehiculo
    path('VehiculoVent', listVehiculoventa, name='listVehiculoventa'),
    path('vehiculoventnuevo', VehiculoventaCreate, name='VehiculoventaCreate'),
    path('vehiventact/<int:id_vehiculoventa>/', VehiculoventaEdit, name='VehiculoventaEdit'),
    path('vehiventelim/<int:id_vehiculoventa>/', VehiculoventaElim, name='VehiculoventaElim'),

    #Consultas
    path('consulta/', consulta1, name='consulta1'),
    path('consulta2/', consulta2, name='consulta2'),
    path('consulta3/', consulta3, name='consulta3'),
    path('consulta4/', consulta4, name='consulta4'),
]