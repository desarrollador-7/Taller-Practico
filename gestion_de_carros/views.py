from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from .forms import *
from braces.views import PermissionRequiredMixin, MultiplePermissionsRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

#1. Utilizar los permisos en el views.py 
#2. Tenemos que crear el html de donde se va a extender el menú
#3. Mejora: Crear el modelo para gestionar los permisos y los roles. 
#4. login: para identificar los permisos que tiene cada usuario
#Tarea: (Listado de roles que se pueden utilizar en esta aplicación)



class ListaCarro(MultiplePermissionsRequiredMixin, ListView):
    """Clase para proporcionar una vista que muestra una lista de objetos.

    :param ListView: Permite visualizar una vista
    :type ListView: Objeto
    """       
    
    model = Carro
    template_name = 'gestion_carros/listado_carros.html'
    context_object_name = 'carros' 
    permissions = {"any": ('gestion_de_carros.listar_carros', 'gestion_de_carros.actualizar_carro', 'gestion_de_carros.eliminar_carro', 'gestion_de_carros.detalle_carro' )}
    

class VistaCarro(PermissionRequiredMixin, DetailView):
    """Clase para mostrar la información detallada de un objeto específico.

    :param DetailView: visualiza los detalles de un objeto.
    :type DetailView: Objeto
    """    
    
    model = Carro
    template_name = 'gestion_carros/vista_carro.html'
    permission_required = 'gestion_de_carros.detalle_carro'
    success_url = reverse_lazy('carros')

class CrearCarro(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    """Clase que permite la creación de un nuevo objeto en la base de datos.

    :param CreateView: Maneja la creacion de objetos
    :type CreateView: Objeto
    """    
    
    model = Carro
    form_class = CarroForm
    template_name = 'gestion_carros/crear_carro.html'
    permission_required = 'gestion_de_carros.crear_carro'
    success_url = reverse_lazy('listado_carros')
    success_message = "El carro %(placa)s fue creado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        form = super().form_invalid(form)
        try:
            if form:
               messages.success(self.request, self.success_message)
        except Exception:
            messages.error(self.request, "No se pudo crear el carro. Por favor, revise los datos.")
        return form
        
class ActualizarCarro(PermissionRequiredMixin,SuccessMessageMixin, UpdateView):
    """Clase que permite la ctualización de los datos de un objeto específico.

    :param UpdateView: Manejar actualizaciones de objetos.
    :type UpdateView: Objeto
    """       
    
    model = Carro
    form_class = CarroForm
    template_name= 'gestion_carros/crear_carro.html'
    permission_required = 'gestion_de_carros.actualizar_carro'
    success_url = reverse_lazy('listado_carros')
    success_message = "El carro %(placa)s fue actualizado exitosamente"
    
    def form_invalid(self, form):
        """Se ejecuta cuando el formulario es inválido"""
        messages.error(self.request, "No se pudo actualizar el carro. Por favor, revise los datos.")
        return super().form_invalid(form)
    
    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return self.success_url
    
    
class EliminarCarro(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    """Clase que proporcionar una interfaz para la eliminación de un objeto.

    :param DeleteView: Gestiona la eliminación de objetos.
    :type DeleteView: Objeto
    """       
    
    model = Carro
    template_name = 'gestion_carros/eliminar_carro.html'
    permission_required = 'gestion_de_carros.eliminar_carro'
    success_url = reverse_lazy('listado_carros')
    
    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            placa = self.object.placa 
            result = super().delete(request, *args, **kwargs)
            messages.success(self.request, f"El carro con placa {placa} fue eliminado exitosamente")
            return result
            
        except Exception:
            # Si hay algún error durante la eliminación
            messages.error(
                self.request, 
                f"No se pudo eliminar el carro con placa {placa}. Tiene una relacion."
            )
            # Redirigimos de vuelta a la lista de carros
            return HttpResponseRedirect(self.success_url)