from django.shortcuts import render, redirect
from apps.vehiculos.models import Vehiculo, Marca, TipoVehiculo #importo la clase que usaré
# aquí es donde hago las consultas
from apps.vehiculos.formVehiculo import VehiculoForm
from apps.vehiculos.formMarca import MarcaForm
from apps.vehiculos.formTipoVehiculo import TipoVehiculoForm

def listVehiculos(request):
    vehiculos = Vehiculo.objects.all().order_by('id') # ordena de forma descendente por el id
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

def vehiculoEdit(request, id_vehiculo):

    vehiculo= Vehiculo.objects.get(pk=id_vehiculo)

    if request.method == 'GET':
        form = VehiculoForm(instance=vehiculo) #clase que importo desde el archivo formVehiculo.py
    else:
        form =VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
        
        return redirect('vehiculos:listVehiculos')

    return render(request,'vehiculos/vehiculo_form.html', {'form': form})



def vehiculoElim(request, id_vehiculo):

    vehiculo= Vehiculo.objects.get(pk=id_vehiculo)

    if request.method == 'POST':
        vehiculo.delete() #es que se usa para eliminar un elemento de la base de datos
        return redirect('vehiculos:listVehiculos')
    
    return render(request,'vehiculos/vehiculoElimform.html', {'vehiculos': vehiculo})


#--------------------------------------
#---------------Marcas-----------------
#--------------------------------------


def listMarca(request):
    marca = Marca.objects.all().order_by('id') # ordena de forma descendente por el id
    context = {'vehiculos':marca} # creo una variable que se llama vehiculos: y luego a esa variable le asigno la lista de todos los vehiculos y esa se llama vehiculos, la que creé anteriormente
    #context contiene el listado de los vehiculos
    return render(request, 'marcas/listMarca.html', context)

def marcaCreate(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST) #clase que importo desde el archivo formVehiculo.py
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listMarca') #el enlace que puse en base.html cuando va a vehiculos
    else:
        form =MarcaForm()
        return render(request,'marcas/marca_form.html', {'form': form})

def marcaEdit(request, id_marca):

    marca= Marca.objects.get(pk=id_marca)

    if request.method == 'GET':
        form = MarcaForm(instance=marca) #clase que importo desde el archivo formVehiculo.py
    else:
        form =MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
        
        return redirect('vehiculos:listMarca')

    return render(request,'marcas/marca_form.html', {'form': form})

def marcaElim(request, id_marca):

    marca= Marca.objects.get(pk=id_marca)

    if request.method == 'POST':
        marca.delete() #es que se usa para eliminar un elemento de la base de datos
        return redirect('vehiculos:listMarca')
    
    return render(request,'marcas/marcaElimform.html', {'marca': marca})


#---------------------------------------------
#---------------Tipo Vehiculo-----------------
#---------------------------------------------

def listTipoVehiculo(request):
    tipovehiculo = TipoVehiculo.objects.all().order_by('id') # ordena de forma descendente por el id
    context = {'vehiculos':tipovehiculo} # creo una variable que se llama vehiculos: y luego a esa variable le asigno la lista de todos los vehiculos y esa se llama vehiculos, la que creé anteriormente
    #context contiene el listado de los vehiculos
    return render(request, 'tipovehiculos/listTipoVehiculo.html', context)

def TipoVehiculoCreate(request):
    if request.method == 'POST':
        form = TipoVehiculoForm(request.POST) #clase que importo desde el archivo formVehiculo.py
        if form.is_valid():
            form.save()
        return redirect('vehiculos:listTipoVehiculo') #el enlace que puse en base.html cuando va a vehiculos
    else:
        form =TipoVehiculoForm()
        return render(request,'tipovehiculos/tipovehiculo_form.html', {'form': form})

def TipoVehiculoEdit(request, id_tipovehiculo):

    tipovehiculo= TipoVehiculo.objects.get(pk=id_tipovehiculo)

    if request.method == 'GET':
        form = MarcaForm(instance=tipovehiculo) #clase que importo desde el archivo formVehiculo.py
    else:
        form =MarcaForm(request.POST, instance=tipovehiculo)
        if form.is_valid():
            form.save()
        
        return redirect('vehiculos:listTipoVehiculo')

    return render(request,'tipovehiculos/tipovehiculo_form.html', {'form': form})

def TipoVehiculoElim(request, id_tipovehiculo):

    tipovehiculo= TipoVehiculo.objects.get(pk=id_tipovehiculo)

    if request.method == 'POST':
        tipovehiculo.delete() #es que se usa para eliminar un elemento de la base de datos
        return redirect('vehiculos:listTipoVehiculo')
    
    return render(request,'tipovehiculos/listTipoVehiculoElimform.html', {'tipovehiculo': tipovehiculo})