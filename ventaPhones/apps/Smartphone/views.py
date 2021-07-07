from re import template
from django.shortcuts import render
from django.http import HttpResponse
from apps.Smartphone.models import Smartphone
# Create your views here.
from .forms import SmartphoneForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# def base(request):
    
#     context = {'smartphones': Smartphone.objects.all}
#     return render(request, 'base.html', context)

def ok(request):
    
    context = {'smartphones': Smartphone.objects.all}
    return render(request, 'home.html', context)




class SmartphoneList(ListView):
    model = Smartphone
    template_name = 'Smartphone/list_smartphone.html'
    
    
class SmartphoneUpdate(UpdateView):
    model = Smartphone
    form_class = SmartphoneForm
    template_name = 'Smartphone/form_smartphone.html'
    success_url = reverse_lazy('list_smartphones')
    
class SmartphoneDelete(DeleteView):
    model = Smartphone
    template_name = 'Smartphone/delete_smartphone.html'
    success_url = reverse_lazy('list_smartphones')


class SmartphoneListCliente(ListView):
    model = Smartphone
    template_name = 'Smartphone/cliente_smartphone.html'
    
    