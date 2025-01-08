from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 
from .models import *
from .forms import *
from django.contrib.auth.mixins import PermissionRequiredMixin


class ListaCarro(ListView):
    model = Carro
    template_name = 'listado_carros.html'
    context_object_name = 'carros' 
    

class CrearCarro(CreateView):
    model = Carro
    form_class = CarroForm
    template_name = 'crear_carro.html'
    success_url = reverse_lazy('listado_carros')
    
class ActualizarCarro(UpdateView):
    model = Carro
    form_class = CarroForm
    template_name= 'crear_carro.html'
    success_url = reverse_lazy('listado_carros')
    
    
class EliminarCarro(DeleteView):
    model = Carro
    template_name = 'eliminar_carro.html'
    success_url = reverse_lazy('listado_carros')