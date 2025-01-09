from django.urls import path
from .views import *

urlpatterns = [
    ###Carro
    path("listado_propietarios", ListaPropietario.as_view(), name='listado_propietarios'),
    path("crear_propietario", CrearPropietario.as_view(), name='crear_propietario'),
    path("actualizar_propietario/<int:pk>/", ActualizarPropietario.as_view(), name='actualizar_propietario'),
    path("vista_propietario/<int:pk>/", VistaPropietario.as_view(), name='vista_propietario'),
    path("eliminar_propietario/<int:pk>/", EliminarPropietario.as_view(), name='eliminar_propietario'),   
]