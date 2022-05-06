from django.shortcuts import render, redirect
from apps.vehiculos.models import Vehiculo #importo la clase que usaré
# aquí es donde hago las consultas
from apps.vehiculos.formVehiculo import VehiculoForm
def listVehiculos(request):
    vehiculos = Vehiculo.objects.all().order_by('-id') # ordena de forma descendente por el id
    context = {'vehiculos':vehiculos} # creo una variable que se llama vehiculos: y luego a esa variable le asigno la lista de todos los vehiculos y esa se llama vehiculos, la que creé anteriormente
    #context contiene el listado de los vehiculos
    return render(request, 'vehiculos/listVehiculos.html', context) #aquí estoy renderizando, luego en '' pongo la pagina html que crearé para mostrar esta vista y luego le mando el contexto, que es context

def home (request):
    return render(request, 'base/base.html')

def vehiculoCreate(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST) #clase que importo desde el archivo formVehiculo.py
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listVehiculos') #el enlace que puse en base.html cuando va a vehiculos
    else:
        form =VehiculoForm()
        return render(request,'vehiculos/vehiculo_form.html', {'form': form})
        