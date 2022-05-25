from django import forms
from apps.ventas.models import VehiculoVenta

class vehiculoventaForm(forms.ModelForm):
    class Meta:
        model = VehiculoVenta
        #Es una lista
        fields = [
            'vehiculo',
            'venta',
            'cantidad',
            'precio',
        ]
        #Es un objeto y pongo llave: valor
        labels = {
            'vehiculo': 'Seleccione el vehiculo',
            'venta': 'Seleccione el valor de la venta',
            'cantidad': 'Ingrese la cantidad',
            'precio': 'Ingrese el precio',
        }

        widgets ={
            'vehiculo':forms.Select(attrs={'class': 'form-control'}),
            'venta': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
        }