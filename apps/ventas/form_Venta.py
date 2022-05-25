from django import forms
from apps.ventas.models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        #Es una lista
        fields = [
            'fecha',
            'valorTotal',
            'tipoPago',
            'user',
            #'vehiculo',
        ]
        #Es un objeto y pongo llave: valor
        labels = {
            'fecha': 'Ingrese la fecha',
            'valorTotal': 'Ingrese el valor total',
            'tipoPago': 'Ingrese el tipo de pago',
            'user': 'Seleccione el usuario',
            #'vehiculo': 'Seleccione la vehiculo',
        }

        widgets ={
            'fecha': forms.TextInput(attrs={'class': 'form-control'}),
            'valorTotal': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoPago': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            #'vehiculo': forms.Select(attrs={'class': 'form-control'}),
        }