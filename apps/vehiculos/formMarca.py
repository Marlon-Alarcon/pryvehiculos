from django import forms
from apps.vehiculos.models import Marca

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        #Es una lista
        fields = [
            'nombre',
        ]
        #Es un objeto y pongo llave: valor
        labels = {
            'nombre': 'Ingrese la marca',
        }

        widgets ={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }