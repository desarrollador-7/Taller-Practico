from django.urls import path
from .views import *

urlpatterns = [
    ####--------Usuarios--------####
    path("listado_usuarios", ListaUsuario.as_view(), name='listado_usuarios'),
    path("registrar_usuario", CrearUsuario.as_view(), name='registrar_usuario'),
    path("actualizar_usuario/<int:pk>/", ActualizarUsuario.as_view(), name='actualizar_usuario'),
    path("detalle_usuario/<int:pk>/", VistaUsuario.as_view(), name='detalle_usuario'),
    path("eliminar_usuario/<int:pk>/", EliminarUsuario.as_view(), name='eliminar_usuario'),   
]