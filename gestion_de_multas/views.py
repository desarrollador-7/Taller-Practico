from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from .forms import *
from django.contrib.auth.mixins import PermissionRequiredMixin


class ListaMulta(ListView):
    """Clase para proporcionar una vista que muestra una lista de objetos.

    :param ListView: Permite visualizar una vista
    :type ListView: Objeto
    """       
    
    model = Multas
    template_name = 'listado_multas.html'
    context_object_name = 'multas' 
    

class VistaMulta(DetailView):
    """Clase para mostrar la información detallada de un objeto específico.

    :param DetailView: visualiza los detalles de un objeto.
    :type DetailView: Objeto
    """    
    
    model = Multas
    template_name = 'vista_multa.html'
    success_url = reverse_lazy('multas')
    
class CrearMulta(CreateView):
    """Clase que permite la creación de un nuevo objeto en la base de datos.

    :param CreateView: Maneja la creacion de objetos
    :type CreateView: Objeto
    """    
    
    model = Multas
    form_class = MultasForm
    template_name = 'crear_multa.html'
    success_url = reverse_lazy('listado_multas')
    
class ActualizarMulta(UpdateView):
    """Clase que permite la ctualización de los datos de un objeto específico.

    :param UpdateView: Manejar actualizaciones de objetos.
    :type UpdateView: Objeto
    """       
    
    model = Multas
    form_class = MultasForm
    template_name= 'crear_multa.html'
    success_url = reverse_lazy('listado_multas')
    
    
class EliminarMulta(DeleteView):
    """Clase que proporcionar una interfaz para la eliminación de un objeto.

    :param DeleteView: Gestiona la eliminación de objetos.
    :type DeleteView: Objeto
    """       
    
    model = Multas
    template_name = 'eliminar_multa.html'
    success_url = reverse_lazy('listado_multas')