from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from .forms import *
from django.contrib.auth.mixins import PermissionRequiredMixin


class ListaPropietario(ListView):
    model = Propietario
    template_name = 'listado_propietarios.html'
    context_object_name = 'propietarios' 
    

class VistaPropietario(DetailView):
    model = Propietario
    template_name = 'vista_propietario.html'
    success_url = reverse_lazy('propietarios')
    
class CrearPropietario(CreateView):
    model = Propietario
    form_class = PropietarioForm
    template_name = 'crear_propietario.html'
    success_url = reverse_lazy('listado_propietarios')
    
class ActualizarPropietario(UpdateView):
    model = Propietario
    form_class = PropietarioForm
    template_name= 'crear_propietario.html'
    success_url = reverse_lazy('listado_propietarios')
    
    
class EliminarPropietario(DeleteView):
    model = Propietario
    template_name = 'eliminar_propietario.html'
    success_url = reverse_lazy('listado_propietarios')