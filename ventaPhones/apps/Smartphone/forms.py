

from django.forms import widgets
from django.forms.fields import ImageField
from .models import Smartphone
from django import forms

class SmartphoneForm(forms.ModelForm):
    class Meta:
        model = Smartphone
        
        fields = (
            'image',
            'nombre',
            'precio',
            'color',
            'almacenamiento',
        )
    
        labels = {
            'image':'Imagen Producto',
            'nombre': 'Nombre Producto',
            'precio': 'Precio en CLP',
            'color': 'Color iPhone',
            'almacenamiento': 'Almacenamiento'
        }
        
        widgets = {
            'image':forms.FileInput(attrs={'class':'form-control','type':'file'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'precio':forms.TextInput(attrs={'class':'form-control'}),
            'color':forms.Select(choices="COLORES_OPCIONES" ,attrs={'class':'form-control'}),
            'almacenamiento':forms.Select(choices="ALMACENAMIENTO_OPCIONES",attrs={'class':'form-control'}),
        }
    
    
