from django.shortcuts import render
from django.http import HttpResponse
from apps.Smartphone.models import Smartphone
# Create your views here.

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

    
    