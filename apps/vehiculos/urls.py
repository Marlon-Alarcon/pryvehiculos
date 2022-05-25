from django.urls import path
from apps.vehiculos.views import listVehiculos, vehiculoCreate, vehiculoEdit, vehiculoElim, listMarca, marcaCreate, marcaEdit, marcaElim, listTipoVehiculo, TipoVehiculoCreate, TipoVehiculoEdit,TipoVehiculoElim

app_name='vehiculos' #este el nombre que puse en namespace del archivo urls.py de pryvehiculos
urlpatterns = [
    path('', listVehiculos, name='listVehiculos'), # cuando digan vehiculo/ ejecuta el método listVehiculos
    path('nuevo/', vehiculoCreate, name='vehiculoCreate'),
    path('actualizar/<int:id_vehiculo>/', vehiculoEdit, name='vehiculoEdit'), 
    path('eliminar/<int:id_vehiculo>/', vehiculoElim, name='vehiculoElim'), 

    path('marca/', listMarca, name='listMarca'),
    path('nmarca/', marcaCreate, name='marcaCreate'),
    path('actmarca/<int:id_marca>/', marcaEdit, name='marcaEdit'),
    path('elimmarca/<int:id_marca>/', marcaElim, name='marcaElim'),

    path('tipo/', listTipoVehiculo, name='listTipoVehiculo'),
    path('ntipo/', TipoVehiculoCreate, name='TipoVehiculoCreate'),
    path('actipovehi/<int:id_tipovehiculo>/', TipoVehiculoEdit, name='TipoVehiculoEdit'), 
    path('elimtipovehi/<int:id_tipovehiculo>/', TipoVehiculoElim, name='TipoVehiculoElim'), 
    ]

    


