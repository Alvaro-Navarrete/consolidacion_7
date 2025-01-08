from django.db import models
from datetime import date
from django.core.validators import MinValueValidator

class Laboratorio(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=25)
        
class DirectorGeneral(models.Model):
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField('Laboratorio', on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=30, default='General')
    

class Producto(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey('Laboratorio', on_delete=models.CASCADE)
    f_fabricacion = models.DateField(
        validators=[MinValueValidator(date(2015,1,1))]
    )
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)