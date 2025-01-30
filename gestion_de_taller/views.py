from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from .forms import *
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages



####--------Taller--------####
class ListaTaller(ListView):
    """Clase para proporcionar una vista que muestra una lista de objetos.

    :param ListView: Permite visualizar una vista
    :type ListView: Objeto
    """       
    
    model = Taller
    template_name = 'gestion_taller/listado_talleres.html'
    context_object_name = 'talleres' 
    

class VistaTaller(DetailView):
    """Clase para mostrar la información detallada de un objeto específico.

    :param DetailView: visualiza los detalles de un objeto.
    :type DetailView: Objeto
    """    
    
    model = Taller
    template_name = 'gestion_taller/vista_taller.html'
    success_url = reverse_lazy('talleres')
    
class CrearTaller(SuccessMessageMixin, CreateView):
    """Clase que permite la creación de un nuevo objeto en la base de datos.

    :param CreateView: Maneja la creacion de objetos
    :type CreateView: Objeto
    """    
    
    model = Taller
    form_class = TallerForm
    template_name = 'gestion_taller/crear_taller.html'
    success_url = reverse_lazy('listado_talleres')
    success_message = "El Taller fue creado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        messages.error(self.request, "No se pudo crear el Taller. Por favor, revise los datos.")
        return super().form_invalid(form)
    
class ActualizarTaller(SuccessMessageMixin, UpdateView):
    """Clase que permite la ctualización de los datos de un objeto específico.

    :param UpdateView: Manejar actualizaciones de objetos.
    :type UpdateView: Objeto
    """       
    
    model = Taller
    form_class = TallerForm
    template_name= 'gestion_taller/crear_taller.html'
    success_url = reverse_lazy('listado_talleres')
    success_message = "El Taller fue actualizado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        messages.error(self.request, "No se pudo actualizar el Taller. Por favor, revise los datos.")
        return super().form_invalid(form)
    
    
class EliminarTaller(SuccessMessageMixin, DeleteView):
    """Clase que proporcionar una interfaz para la eliminación de un objeto.

    :param DeleteView: Gestiona la eliminación de objetos.
    :type DeleteView: Objeto
    """       
    
    model = Taller
    template_name = 'gestion_taller/eliminar_taller.html'
    success_url = reverse_lazy('listado_talleres')
    
    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            nombre = self.object.nombre 
            result = super().delete(request, *args, **kwargs)
            messages.success(self.request, f"El Taller {str(nombre)} fue eliminado exitosamente")
            return result
            
        except Exception as e:
            # Si hay algún error durante la eliminación
            messages.error(
                self.request, 
                f"No se pudo eliminar el Taller {str(nombre)}. Tiene una relacion."
            )
            # Redirigimos de vuelta a la lista de carros
            return HttpResponseRedirect(self.success_url)


####--------Mantenimiento--------####
class ListaMantenimiento(ListView):
    """Clase para proporcionar una vista que muestra una lista de objetos.

    :param ListView: Permite visualizar una vista
    :type ListView: Objeto
    """       
    
    model = Mantenimiento
    template_name = 'gestion_taller/listado_mantenimiento.html'
    context_object_name = 'mantenimientos' 
    

class VistaMantenimiento(DetailView):
    """Clase para mostrar la información detallada de un objeto específico.

    :param DetailView: visualiza los detalles de un objeto.
    :type DetailView: Objeto
    """    
    
    model = Mantenimiento
    template_name = 'gestion_taller/vista_mantenimiento.html'
    success_url = reverse_lazy('mantenimientos')
    
class CrearMantenimiento(SuccessMessageMixin, CreateView):
    """Clase que permite la creación de un nuevo objeto en la base de datos.

    :param CreateView: Maneja la creacion de objetos
    :type CreateView: Objeto
    """    
    
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'gestion_taller/crear_mantenimiento.html'
    success_url = reverse_lazy('listado_mantenimientos')
    success_message = "El Mantenimiento fue creado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        messages.error(self.request, "No se pudo crear el Mantenimiento. Por favor, revise los datos.")
        return super().form_invalid(form)
    
class ActualizarMantenimiento(SuccessMessageMixin, UpdateView):
    """Clase que permite la ctualización de los datos de un objeto específico.

    :param UpdateView: Manejar actualizaciones de objetos.
    :type UpdateView: Objeto
    """       
    
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name= 'gestion_taller/crear_mantenimiento.html'
    success_url = reverse_lazy('listado_mantenimientos')
    success_message = "El Mantenimiento fue actualizado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        messages.error(self.request, "No se pudo actualizar el Mantenimiento. Por favor, revise los datos.")
        return super().form_invalid(form)
    
    
class EliminarMantenimiento(SuccessMessageMixin, DeleteView):
    """Clase que proporcionar una interfaz para la eliminación de un objeto.

    :param DeleteView: Gestiona la eliminación de objetos.
    :type DeleteView: Objeto
    """       
    
    model = Mantenimiento
    template_name = 'gestion_taller/eliminar_mantenimiento.html'
    success_url = reverse_lazy('listado_mantenimientos')
    
    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            idn = self.object.idn 
            result = super().delete(request, *args, **kwargs)
            messages.success(self.request, f"El Mantenimiento con id {idn} fue eliminado exitosamente")
            return result
            
        except Exception as e:
            # Si hay algún error durante la eliminación
            messages.error(
                self.request, 
                f"No se pudo eliminar el Mantenimiento con id {idn}. Tiene una relacion."
            )
            # Redirigimos de vuelta a la lista de carros
            return HttpResponseRedirect(self.success_url)