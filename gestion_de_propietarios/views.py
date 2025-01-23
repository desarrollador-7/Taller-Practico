from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
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
    success_message = "El propietario de la matricula %(placa)s fue creado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        messages.error(self.request, "No se pudo crear el propietario. Por favor, revise los datos.")
        return super().form_invalid(form)
    
    
class ActualizarPropietario(SuccessMessageMixin, UpdateView):
    """Clase que permite la ctualización de los datos de un objeto específico.

    :param UpdateView: Manejar actualizaciones de objetos.
    :type UpdateView: Objeto
    """  
    
    model = Propietario
    form_class = PropietarioForm
    template_name= 'crear_propietario.html'
    success_url = reverse_lazy('listado_propietarios')
    success_message = "El propietario de la matricula %(placa)s fue actualizado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        messages.error(self.request, "No se pudo actualizar el propietario. Por favor, revise los datos.")
        return super().form_invalid(form)
    
    
class EliminarPropietario(SuccessMessageMixin, DeleteView):
    """Clase que proporcionar una interfaz para la eliminación de un objeto.

    :param DeleteView: Gestiona la eliminación de objetos.
    :type DeleteView: Objeto
    """ 
    
    model = Propietario
    template_name = 'eliminar_propietario.html'
    success_url = reverse_lazy('listado_propietarios')
    
    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            nombre = self.object.nombre 
            result = super().delete(request, *args, **kwargs)
            messages.success(self.request, f"El propietario con nombre {nombre} fue eliminado exitosamente")
            return result
            
        except Exception as e:
            # Si hay algún error durante la eliminación
            messages.error(
                self.request, 
                "No se pudo eliminar el propietario con nombre {nombre}. Tiene una relacion."
            )
            # Redirigimos de vuelta a la lista de carros
            return HttpResponseRedirect(self.success_url)


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
    


class CrearLicencia(SuccessMessageMixin, CreateView):
    """Clase que permite la creación de un nuevo objeto en la base de datos.

    :param CreateView: Maneja la creacion de objetos
    :type CreateView: Objeto
    """ 
    
    model = Licencia
    form_class = LicenciaForm
    template_name = 'crear_licencia.html'
    success_url = reverse_lazy('listado_licencias')
    success_message = "La licencia fue creada exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        messages.error(self.request, "No se pudo crear la licencia. Por favor, revise los datos.")
        return super().form_invalid(form)
    
    
class ActualizarLicencia(SuccessMessageMixin, UpdateView):
    """Clase que permite la ctualización de los datos de un objeto específico.

    :param UpdateView: Manejar actualizaciones de objetos.
    :type UpdateView: Objeto
    """  
    
    model = Licencia
    form_class = LicenciaForm
    template_name= 'crear_licencia.html'
    success_url = reverse_lazy('listado_licencias')
    success_message = "La licencia con el fue actualizada exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        messages.error(self.request, "No se pudo actualizar la licencia. Por favor, revise los datos.")
        return super().form_invalid(form)
    
    
class EliminarLicencia(SuccessMessageMixin, DeleteView):
    """Clase que proporcionar una interfaz para la eliminación de un objeto.

    :param DeleteView: Gestiona la eliminación de objetos.
    :type DeleteView: Objeto
    """ 
    
    model = Licencia
    template_name = 'eliminar_Licencia.html'
    success_url = reverse_lazy('listado_licencias')
    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            numero = self.object.numero 
            result = super().delete(request, *args, **kwargs)
            messages.success(self.request, f"La licencia con #{numero} fue eliminado exitosamente")
            return result
            
        except Exception as e:
            # Si hay algún error durante la eliminación
            messages.error(
                self.request, 
                "No se pudo eliminar la licencia con #{numero}. Tiene una relacion."
            )
            # Redirigimos de vuelta a la lista de carros
            return HttpResponseRedirect(self.success_url)