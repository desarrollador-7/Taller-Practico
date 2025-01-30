from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from .forms import *
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages



####--------Aseguradora--------####
class ListaAseguradora(ListView):
    """Clase para proporcionar una vista que muestra una lista de objetos.

    :param ListView: Permite visualizar una vista
    :type ListView: Objeto
    """       
    
    model = Aseguradora
    template_name = 'gestion_seguiros/listado_aseguradoras.html'
    context_object_name = 'aseguradoras' 
    

class VistaAseguradora(DetailView):
    """Clase para mostrar la información detallada de un objeto específico.

    :param DetailView: visualiza los detalles de un objeto.
    :type DetailView: Objeto
    """    
    
    model = Aseguradora
    template_name = 'gestion_seguiros/vista_aseguradora.html'
    success_url = reverse_lazy('aseguradoras')
    
class CrearAseguradora(SuccessMessageMixin, CreateView):
    """Clase que permite la creación de un nuevo objeto en la base de datos.

    :param CreateView: Maneja la creacion de objetos
    :type CreateView: Objeto
    """    
    
    model = Aseguradora
    form_class = AseguradoraForm
    template_name = 'gestion_seguiros/crear_aseguradora.html'
    success_url = reverse_lazy('listado_aseguradoras')
    success_message = "La Aseguradora fue creado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        messages.error(self.request, "No se pudo crear la Aseguradora. Por favor, revise los datos.")
        return super().form_invalid(form)
    
class ActualizarAseguradora(SuccessMessageMixin, UpdateView):
    """Clase que permite la ctualización de los datos de un objeto específico.

    :param UpdateView: Manejar actualizaciones de objetos.
    :type UpdateView: Objeto
    """       
    
    model = Aseguradora
    form_class = AseguradoraForm
    template_name= 'gestion_seguiros/crear_aseguradora.html'
    success_url = reverse_lazy('listado_aseguradoras')
    success_message = "La Aseguradora fue actualizada exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        messages.error(self.request, "No se pudo actualizar la Aseguradora. Por favor, revise los datos.")
        return super().form_invalid(form)
    
    
class EliminarAseguradora(SuccessMessageMixin, DeleteView):
    """Clase que proporcionar una interfaz para la eliminación de un objeto.

    :param DeleteView: Gestiona la eliminación de objetos.
    :type DeleteView: Objeto
    """       
    
    model = Aseguradora
    template_name = 'gestion_seguiros/eliminar_aseguradora.html'
    success_url = reverse_lazy('listado_aseguradoras')
    
    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            id_aseguradora = self.object.id_aseguradora 
            result = super().delete(request, *args, **kwargs)
            messages.success(self.request, f"La Aseguradora {id_aseguradora} fue eliminado exitosamente")
            return result
            
        except Exception as e:
            # Si hay algún error durante la eliminación
            messages.error(
                self.request, 
                f"No se pudo eliminar la aseguradora {id_aseguradora}. Tiene una relacion."
            )
            # Redirigimos de vuelta a la lista de carros
            return HttpResponseRedirect(self.success_url)


####--------Seguros--------####
class ListaSeguros(ListView):
    """Clase para proporcionar una vista que muestra una lista de objetos.

    :param ListView: Permite visualizar una vista
    :type ListView: Objeto
    """       
    
    model = Seguro
    template_name = 'gestion_seguiros/listado_seguros.html'
    context_object_name = 'seguros' 
    

class VistaSeguro(DetailView):
    """Clase para mostrar la información detallada de un objeto específico.

    :param DetailView: visualiza los detalles de un objeto.
    :type DetailView: Objeto
    """    
    
    model = Seguro
    template_name = 'gestion_seguiros/vista_seguro.html'
    success_url = reverse_lazy('seguros')
    
class CrearSeguro(SuccessMessageMixin, CreateView):
    """Clase que permite la creación de un nuevo objeto en la base de datos.

    :param CreateView: Maneja la creacion de objetos
    :type CreateView: Objeto
    """    
    
    model = Seguro
    form_class = SeguroForm
    template_name = 'gestion_seguiros/crear_seguro.html'
    success_url = reverse_lazy('listado_seguros')
    success_message = "El Seguro fue creado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        messages.error(self.request, "No se pudo crear el Seguro. Por favor, revise los datos.")
        return super().form_invalid(form)
    
class ActualizarSeguro(SuccessMessageMixin, UpdateView):
    """Clase que permite la ctualización de los datos de un objeto específico.

    :param UpdateView: Manejar actualizaciones de objetos.
    :type UpdateView: Objeto
    """       
    
    model = Seguro
    form_class = SeguroForm
    template_name= 'gestion_seguiros/crear_seguro.html'
    success_url = reverse_lazy('listado_seguros')
    success_message = "El Seguro fue actualizado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        messages.error(self.request, "No se pudo actualizar el Seguro. Por favor, revise los datos.")
        return super().form_invalid(form)
    
    
class EliminarSeguro(SuccessMessageMixin, DeleteView):
    """Clase que proporcionar una interfaz para la eliminación de un objeto.

    :param DeleteView: Gestiona la eliminación de objetos.
    :type DeleteView: Objeto
    """       
    
    model = Seguro
    template_name = 'gestion_seguiros/eliminar_seguro.html'
    success_url = reverse_lazy('listado_seguros')
    
    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            dni = self.object.dni 
            result = super().delete(request, *args, **kwargs)
            messages.success(self.request, f"El Seguro con id {dni} fue eliminado exitosamente")
            return result
            
        except Exception as e:
            # Si hay algún error durante la eliminación
            messages.error(
                self.request, 
                f"No se pudo eliminar el Seguro con id {dni}. Tiene una relacion."
            )
            # Redirigimos de vuelta a la lista de carros
            return HttpResponseRedirect(self.success_url)