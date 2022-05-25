from django.shortcuts import render, redirect
from apps.ventas.models import Venta, VehiculoVenta
from apps.ventas.form_Venta import VentaForm
from apps.ventas.form_VehiculoVenta import vehiculoventaForm

def listVentas(request):
    ventas = Venta.objects.all().order_by('id') # ordena de forma descendente por el id
    context = {'ventas':ventas} # creo una variable que se llama vehiculos: y luego a esa variable le asigno la lista de todos los vehiculos y esa se llama vehiculos, la que creé anteriormente
    #context contiene el listado de los vehiculos
    return render(request, 'ventas/listVentas.html', context) #aquí estoy renderizando, luego en '' pongo la pagina html que crearé para mostrar esta vista y luego le mando el contexto, que es context

def home (request):
    return render(request, 'base/base.html')

def ventaCreate(request):
    if request.method == 'POST':
        form = VentaForm(request.POST) #clase que importo desde el archivo ventaform.py
        if form.is_valid():
            form.save()
        return redirect('ventas:listVentas') #el enlace que puse en base.html cuando va a vehiculos
    else:
        form =VentaForm()
        return render(request,'ventas/venta_form.html', {'form': form})


def ventaEdit(request, id_venta):

    venta= Venta.objects.get(pk=id_venta)

    if request.method == 'GET':
        form = VentaForm(instance=venta) #clase que importo desde el archivo formVehiculo.py
    else:
        form =VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
        
        return redirect('ventas:listVentas')

    return render(request,'ventas/venta_form.html', {'form': form})



def ventaElim(request, id_venta):

    venta= Venta.objects.get(pk=id_venta)

    if request.method == 'POST':
        venta.delete() #clase que importo desde el archivo formVehiculo.py
        return redirect('ventas:listVentas')
    
    return render(request,'ventas/ventaElimform.html', {'ventas': venta})





# Create your views here.

#-------------------------------------
#---------- Vehiculo Venta -----------
#-------------------------------------

def listVehiculoventa(request):
    vehiculosventas = VehiculoVenta.objects.all().order_by('id') # ordena de forma descendente por el id
    context = {'ventas':vehiculosventas} # creo una variable que se llama vehiculos: y luego a esa variable le asigno la lista de todos los vehiculos y esa se llama vehiculos, la que creé anteriormente
    #context contiene el listado de los vehiculos
    return render(request, 'vehiculosventa/listVehiculoVenta.html', context) #aquí estoy renderizando, luego en '' pongo la pagina html que crearé para mostrar esta vista y luego le mando el contexto, que es context


def VehiculoventaCreate(request):
    if request.method == 'POST':
        form = vehiculoventaForm(request.POST) #clase que importo desde el archivo ventaform.py
        if form.is_valid():
            form.save()
        return redirect('ventas:listVehiculoventa') #el enlace que puse en base.html cuando va a vehiculos
    else:
        form =vehiculoventaForm()
        return render(request,'vehiculosventa/vehiculoventa_form.html', {'form': form})


def VehiculoventaEdit(request, id_vehiculoventa):

    vehiculoventa= VehiculoVenta.objects.get(pk=id_vehiculoventa)

    if request.method == 'GET':
        form = vehiculoventaForm(instance=vehiculoventa) #clase que importo desde el archivo formVehiculo.py
    else:
        form =vehiculoventaForm(request.POST, instance=vehiculoventa)
        if form.is_valid():
            form.save()
        
        return redirect('ventas:listVehiculoventa')

    return render(request,'vehiculosventa/vehiculoventa_form.html', {'form': form})



def VehiculoventaElim(request, id_vehiculoventa):

    vehiculoventa= VehiculoVenta.objects.get(pk=id_vehiculoventa)

    if request.method == 'POST':
        vehiculoventa.delete() #clase que importo desde el archivo formVehiculo.py
        return redirect('ventas:listVehiculoventa')
    
    return render(request,'vehiculosventa/vehiculoventaElimform.html', {'vehiculoventa': vehiculoventa})