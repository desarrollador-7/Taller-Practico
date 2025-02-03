from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import FormView, CreateView, UpdateView, ListView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required 



class Login(FormView):
    form_class = LoginForm
    template_name = 'gestion_usuarios/login.html'
    success_url = reverse_lazy('listado_carros')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('listado_carros')
        return super(Login, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        usuario = self.request.user
        if usuario is not None:
            if  not usuario.is_staff and not usuario.is_superuser:
                messages.success(self.request, "Sesión inicia correctamente")
        return super(Login, self).form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Ingrese un Usaurio y una contraseña válido para entrar el sistema")
        return super(Login, self).form_invalid(form)
    

@login_required
def Logout(request):
    logout(request)
    messages.success(request, "Sesión cerrada correctamente")
    return redirect('login')


class Inicio(TemplateView):
    template_name = 'menu_inicial.html'
    
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super(Inicio, self).get(request *args, **kwargs)