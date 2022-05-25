from django.urls import path
from apps.ventas.views import listVentas, ventaCreate, ventaEdit, ventaElim, listVehiculoventa, VehiculoventaCreate, VehiculoventaEdit, VehiculoventaElim

app_name='ventas'
urlpatterns = [
    path('', listVentas, name='listVentas'),
    path('nuevo/', ventaCreate, name='ventaCreate'),
    path('actualizar/<int:id_venta>/', ventaEdit, name='ventaEdit'),
    path('eliminar/<int:id_venta>/', ventaElim, name='ventaElim'),

    path('VehiculoVent', listVehiculoventa, name='listVehiculoventa'),
    path('vehiculoventnuevo', VehiculoventaCreate, name='VehiculoventaCreate'),
    path('vehiventact/<int:id_vehiculoventa>/', VehiculoventaEdit, name='VehiculoventaEdit'),
    path('vehiventelim/<int:id_vehiculoventa>/', VehiculoventaElim, name='VehiculoventaElim'),
]