from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from .forms import *
from django.contrib.auth.mixins import PermissionRequiredMixin



####--------Aseguradora--------####
class ListaAseguradora(ListView):
    """Clase para proporcionar una vista que muestra una lista de objetos.

    :param ListView: Permite visualizar una vista
    :type ListView: Objeto
    """       
    
    model = Aseguradora
    template_name = 'listado_aseguradoras.html'
    context_object_name = 'aseguradoras' 
    

class VistaAseguradora(DetailView):
    """Clase para mostrar la información detallada de un objeto específico.

    :param DetailView: visualiza los detalles de un objeto.
    :type DetailView: Objeto
    """    
    
    model = Aseguradora
    template_name = 'vista_aseguradora.html'
    success_url = reverse_lazy('aseguradoras')
    
class CrearAseguradora(CreateView):
    """Clase que permite la creación de un nuevo objeto en la base de datos.

    :param CreateView: Maneja la creacion de objetos
    :type CreateView: Objeto
    """    
    
    model = Aseguradora
    form_class = AseguradoraForm
    template_name = 'crear_aseguradora.html'
    success_url = reverse_lazy('listado_aseguradoras')
    
class ActualizarAseguradora(UpdateView):
    """Clase que permite la ctualización de los datos de un objeto específico.

    :param UpdateView: Manejar actualizaciones de objetos.
    :type UpdateView: Objeto
    """       
    
    model = Aseguradora
    form_class = AseguradoraForm
    template_name= 'crear_aseguradora.html'
    success_url = reverse_lazy('listado_aseguradoras')
    
    
class EliminarAseguradora(DeleteView):
    """Clase que proporcionar una interfaz para la eliminación de un objeto.

    :param DeleteView: Gestiona la eliminación de objetos.
    :type DeleteView: Objeto
    """       
    
    model = Aseguradora
    template_name = 'eliminar_aseguradora.html'
    success_url = reverse_lazy('listado_aseguradoras')


####--------Seguros--------####
class ListaSeguros(ListView):
    """Clase para proporcionar una vista que muestra una lista de objetos.

    :param ListView: Permite visualizar una vista
    :type ListView: Objeto
    """       
    
    model = Seguro
    template_name = 'listado_seguros.html'
    context_object_name = 'seguros' 
    

class VistaSeguro(DetailView):
    """Clase para mostrar la información detallada de un objeto específico.

    :param DetailView: visualiza los detalles de un objeto.
    :type DetailView: Objeto
    """    
    
    model = Seguro
    template_name = 'vista_seguro.html'
    success_url = reverse_lazy('seguros')
    
class CrearSeguro(CreateView):
    """Clase que permite la creación de un nuevo objeto en la base de datos.

    :param CreateView: Maneja la creacion de objetos
    :type CreateView: Objeto
    """    
    
    model = Seguro
    form_class = SeguroForm
    template_name = 'crear_seguro.html'
    success_url = reverse_lazy('listado_seguros')
    
class ActualizarSeguro(UpdateView):
    """Clase que permite la ctualización de los datos de un objeto específico.

    :param UpdateView: Manejar actualizaciones de objetos.
    :type UpdateView: Objeto
    """       
    
    model = Seguro
    form_class = SeguroForm
    template_name= 'crear_seguro.html'
    success_url = reverse_lazy('listado_seguros')
    
    
class EliminarSeguro(DeleteView):
    """Clase que proporcionar una interfaz para la eliminación de un objeto.

    :param DeleteView: Gestiona la eliminación de objetos.
    :type DeleteView: Objeto
    """       
    
    model = Seguro
    template_name = 'eliminar_seguro.html'
    success_url = reverse_lazy('listado_seguros')