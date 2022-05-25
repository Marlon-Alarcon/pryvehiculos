from django.db import models
from django.contrib.auth.models import User
from apps.vehiculos.models import Vehiculo

# Create your models here.

class Venta(models.Model):
    fecha = models.DateField()
    valorTotal = models.BigIntegerField()
    tipoPago = models.CharField(max_length=20)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    vehiculo = models.ManyToManyField(Vehiculo, through= 'VehiculoVenta')

    def __str__(self):
        return str(self.valorTotal) #[:20] + " "+str(self.valorTotal) -> si deseo agregarle otro dato a la vista

class VehiculoVenta(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete= models.CASCADE, blank=False, null=False)
    venta = models.ForeignKey(Venta, on_delete= models.CASCADE, blank=False, null=False)
    cantidad = models.IntegerField()
    precio = models.BigIntegerField()

