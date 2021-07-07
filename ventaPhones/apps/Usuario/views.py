from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .forms import RegistroForm


# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = 'Usuario/usuario_form.html'
    form_class = RegistroForm
    success_url = reverse_lazy('home')
    
class UserList(ListView):
    model = User
    template_name = 'Usuario/listar_usuarios.html'