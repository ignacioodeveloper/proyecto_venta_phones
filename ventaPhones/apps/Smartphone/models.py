from django.db import models

# Create your models here.

ALMACENTAMIENTO_OPCIONES = (
    ('64','64GB'),
    ('128', '128GB'),
    ('256', '256GB'),
)

COLORES_OPCIONES = (
    ('black', 'black'),
    ('red', 'red'),
    ('white','white'),
    ('blue', 'blue'),
)

class Smartphone(models.Model):
    image = models.ImageField(upload_to='smartphones')
    
    nombre = models.CharField(max_length=25)
    precio = models.IntegerField()
    
    color = models.CharField(choices=COLORES_OPCIONES, default='black', max_length=20)
    
    almacenamiento = models.CharField(choices=ALMACENTAMIENTO_OPCIONES, default='64', max_length=5)
    
    def __str__(self):
        
        return self.nombre