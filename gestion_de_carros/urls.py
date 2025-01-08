from django.urls import path
from .views import *

urlpatterns = [
    ###Carro
    path("listado_carros", ListaCarro.as_view(), name='listado_carros'),
    path("crear_carro", CrearCarro.as_view(), name='crear_carro'),
    path("actualizar_carro/<int:pk>/", ActualizarCarro.as_view(), name='actualizar_carro'),
    path("vista_carro/<int:pk>/", VistaCarro.as_view(), name='vista_carro'),
    path("eliminar_carro/<int:pk>/", EliminarCarro.as_view(), name='eliminar_carro'),   
]