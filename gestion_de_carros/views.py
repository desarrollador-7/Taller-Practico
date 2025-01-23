from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from .forms import *
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class ListaCarro(ListView):
    """Clase para proporcionar una vista que muestra una lista de objetos.

    :param ListView: Permite visualizar una vista
    :type ListView: Objeto
    """       
    
    model = Carro
    template_name = 'listado_carros.html'
    context_object_name = 'carros' 
    

class VistaCarro(DetailView):
    """Clase para mostrar la información detallada de un objeto específico.

    :param DetailView: visualiza los detalles de un objeto.
    :type DetailView: Objeto
    """    
    
    model = Carro
    template_name = 'vista_carro.html'
    success_url = reverse_lazy('carros')

class CrearCarro(SuccessMessageMixin, CreateView):
    """Clase que permite la creación de un nuevo objeto en la base de datos.

    :param CreateView: Maneja la creacion de objetos
    :type CreateView: Objeto
    """    
    
    model = Carro
    form_class = CarroForm
    template_name = 'crear_carro.html'
    success_url = reverse_lazy('listado_carros')
    success_message = "El carro %(placa)s fue creado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        messages.error(self.request, "No se pudo crear el carro. Por favor, revise los datos.")
        return super().form_invalid(form)
    
class ActualizarCarro(SuccessMessageMixin, UpdateView):
    """Clase que permite la ctualización de los datos de un objeto específico.

    :param UpdateView: Manejar actualizaciones de objetos.
    :type UpdateView: Objeto
    """       
    
    model = Carro
    form_class = CarroForm
    template_name= 'crear_carro.html'
    success_url = reverse_lazy('listado_carros')
    success_message = "El carro %(placa)s fue actualizado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        messages.error(self.request, "No se pudo actualizar el carro. Por favor, revise los datos.")
        return super().form_invalid(form)
    
    
class EliminarCarro(SuccessMessageMixin, DeleteView):
    """Clase que proporcionar una interfaz para la eliminación de un objeto.

    :param DeleteView: Gestiona la eliminación de objetos.
    :type DeleteView: Objeto
    """       
    
    model = Carro
    template_name = 'eliminar_carro.html'
    success_url = reverse_lazy('listado_carros')
    
    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            placa = self.object.placa 
            result = super().delete(request, *args, **kwargs)
            messages.success(self.request, f"El carro con placa {placa}s fue eliminado exitosamente")
            return result
            
        except Exception as e:
            # Si hay algún error durante la eliminación
            messages.error(
                self.request, 
                "No se pudo eliminar el carro. Tiene una relacion."
            )
            # Redirigimos de vuelta a la lista de carros
            return HttpResponseRedirect(self.success_url)