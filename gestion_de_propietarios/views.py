from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from .forms import *
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


####--------Propietario--------####
class ListaPropietario(ListView):
    """Clase para proporcionar una vista que muestra una lista de objetos.

    :param ListView: Permite visualizar una vista
    :type ListView: Objeto
    """  
    
    model = Propietario
    template_name = 'listado_propietarios.html'
    context_object_name = 'propietarios' 

class VistaPropietario(DetailView):
    """Clase para mostrar la información detallada de un objeto específico.

    :param DetailView: visualiza los detalles de un objeto.
    :type DetailView: Objeto
    """   
    
    model = Propietario
    template_name = 'vista_propietario.html'
    success_url = reverse_lazy('propietarios')
    


class CrearPropietario(SuccessMessageMixin, CreateView):
    """Clase que permite la creación de un nuevo objeto en la base de datos.

    :param CreateView: Maneja la creacion de objetos
    :type CreateView: Objeto
    """ 
    
    model = Propietario
    form_class = PropietarioForm
    template_name = 'crear_propietario.html'
    success_url = reverse_lazy('listado_propietarios')
    # success_message = "¡El Propietario %(nombre)% fue agregado exitosamente!"
    
    # def form_invalid(self, form):
    #     messages.error(self.request, "Hubo un error al intentar crear un propietario. Por favor verifica los datos.")
    #     return super().form_invalid(form)
    
class ActualizarPropietario(UpdateView):
    """Clase que permite la ctualización de los datos de un objeto específico.

    :param UpdateView: Manejar actualizaciones de objetos.
    :type UpdateView: Objeto
    """  
    
    model = Propietario
    form_class = PropietarioForm
    template_name= 'crear_propietario.html'
    success_url = reverse_lazy('listado_propietarios')
    
    
class EliminarPropietario(DeleteView):
    """Clase que proporcionar una interfaz para la eliminación de un objeto.

    :param DeleteView: Gestiona la eliminación de objetos.
    :type DeleteView: Objeto
    """ 
    
    model = Propietario
    template_name = 'eliminar_propietario.html'
    success_url = reverse_lazy('listado_propietarios')


####--------Licencia--------####
class ListaLicencia(ListView):
    """Clase para proporcionar una vista que muestra una lista de objetos.

    :param ListView: Permite visualizar una vista
    :type ListView: Objeto
    """  
    
    model = Licencia
    template_name = 'listado_licencias.html'
    context_object_name = 'licencias' 

class VistaLicencia(DetailView):
    """Clase para mostrar la información detallada de un objeto específico.

    :param DetailView: visualiza los detalles de un objeto.
    :type DetailView: Objeto
    """   
    
    model = Licencia
    template_name = 'vista_licencia.html'
    success_url = reverse_lazy('licencias')
    


class CrearLicencia(CreateView):
    """Clase que permite la creación de un nuevo objeto en la base de datos.

    :param CreateView: Maneja la creacion de objetos
    :type CreateView: Objeto
    """ 
    
    model = Licencia
    form_class = LicenciaForm
    template_name = 'crear_licencia.html'
    success_url = reverse_lazy('listado_licencias')
    
class ActualizarLicencia(UpdateView):
    """Clase que permite la ctualización de los datos de un objeto específico.

    :param UpdateView: Manejar actualizaciones de objetos.
    :type UpdateView: Objeto
    """  
    
    model = Licencia
    form_class = LicenciaForm
    template_name= 'crear_licencia.html'
    success_url = reverse_lazy('listado_licencias')
    
    
class EliminarLicencia(DeleteView):
    """Clase que proporcionar una interfaz para la eliminación de un objeto.

    :param DeleteView: Gestiona la eliminación de objetos.
    :type DeleteView: Objeto
    """ 
    
    model = Licencia
    template_name = 'eliminar_Licencia.html'
    success_url = reverse_lazy('listado_licencias')