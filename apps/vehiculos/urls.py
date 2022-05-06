from django.urls import path
from apps.vehiculos.views import listVehiculos, vehiculoCreate

app_name='vehiculos' #este el nombre que puse en namespace del archivo urls.py de pryvehiculos
urlpatterns = [
    path('', listVehiculos, name='listVehiculos'), # cuando digan vehiculo/ ejecuta el método listVehiculos
    path('nuevo/', vehiculoCreate, name='vehiculoCreate'), 
    ]


