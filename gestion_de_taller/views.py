from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from .forms import *
from django.contrib.auth.mixins import PermissionRequiredMixin



####--------Taller--------####
class ListaTaller(ListView):
    """Clase para proporcionar una vista que muestra una lista de objetos.

    :param ListView: Permite visualizar una vista
    :type ListView: Objeto
    """       
    
    model = Taller
    template_name = 'listado_talleres.html'
    context_object_name = 'talleres' 
    

class VistaTaller(DetailView):
    """Clase para mostrar la información detallada de un objeto específico.

    :param DetailView: visualiza los detalles de un objeto.
    :type DetailView: Objeto
    """    
    
    model = Taller
    template_name = 'vista_taller.html'
    success_url = reverse_lazy('talleres')
    
class CrearTaller(CreateView):
    """Clase que permite la creación de un nuevo objeto en la base de datos.

    :param CreateView: Maneja la creacion de objetos
    :type CreateView: Objeto
    """    
    
    model = Taller
    form_class = TallerForm
    template_name = 'crear_taller.html'
    success_url = reverse_lazy('listado_talleres')
    
class ActualizarTaller(UpdateView):
    """Clase que permite la ctualización de los datos de un objeto específico.

    :param UpdateView: Manejar actualizaciones de objetos.
    :type UpdateView: Objeto
    """       
    
    model = Taller
    form_class = TallerForm
    template_name= 'crear_taller.html'
    success_url = reverse_lazy('listado_talleres')
    
    
class EliminarTaller(DeleteView):
    """Clase que proporcionar una interfaz para la eliminación de un objeto.

    :param DeleteView: Gestiona la eliminación de objetos.
    :type DeleteView: Objeto
    """       
    
    model = Taller
    template_name = 'eliminar_taller.html'
    success_url = reverse_lazy('listado_talleres')


####--------Mantenimiento--------####
class ListaMantenimiento(ListView):
    """Clase para proporcionar una vista que muestra una lista de objetos.

    :param ListView: Permite visualizar una vista
    :type ListView: Objeto
    """       
    
    model = Mantenimiento
    template_name = 'listado_mantenimiento.html'
    context_object_name = 'mantenimientos' 
    

class VistaMantenimiento(DetailView):
    """Clase para mostrar la información detallada de un objeto específico.

    :param DetailView: visualiza los detalles de un objeto.
    :type DetailView: Objeto
    """    
    
    model = Mantenimiento
    template_name = 'vista_mantenimiento.html'
    success_url = reverse_lazy('mantenimientos')
    
class CrearMantenimiento(CreateView):
    """Clase que permite la creación de un nuevo objeto en la base de datos.

    :param CreateView: Maneja la creacion de objetos
    :type CreateView: Objeto
    """    
    
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'crear_mantenimiento.html'
    success_url = reverse_lazy('listado_mantenimientos')
    
class ActualizarMantenimiento(UpdateView):
    """Clase que permite la ctualización de los datos de un objeto específico.

    :param UpdateView: Manejar actualizaciones de objetos.
    :type UpdateView: Objeto
    """       
    
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name= 'crear_mantenimiento.html'
    success_url = reverse_lazy('listado_mantenimientos')
    
    
class EliminarMantenimiento(DeleteView):
    """Clase que proporcionar una interfaz para la eliminación de un objeto.

    :param DeleteView: Gestiona la eliminación de objetos.
    :type DeleteView: Objeto
    """       
    
    model = Mantenimiento
    template_name = 'eliminar_mantenimiento.html'
    success_url = reverse_lazy('listado_mantenimientos')