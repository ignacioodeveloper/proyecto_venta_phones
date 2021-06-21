from django.db import models

# Create your models here.
# atributos Smartphone
# nombre, precio, color, capacidad, cantidad

class Smartphone(models.Model):
    nombre = models.CharField(max_length=25)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    colores = [
        ('black', 'black'),
        ('red', 'red'),
        ('white', 'white')]
    
    color = models.CharField(choices=colores, default='black', max_length=20)
    
    capacidades = [
        ('64', '64GB'),
        ('128', '128GB')]
    
    cantidad = models.CharField(choices=capacidades, default='64', max_length=5)
    
    
    def __str__(self):
        txt = " Modelo: {0} | Color: {1} | Precio: $ {2} "
        return txt.format(self.nombre,self.color,self.precio)