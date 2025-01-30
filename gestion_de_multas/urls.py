from django.urls import path
from .views import *

urlpatterns = [
    ####--------Multas--------####
    path("listado_multas", ListaMulta.as_view(), name='listado_multas'),
    path("crear_multa", CrearMulta.as_view(), name='crear_multa'),
    path("actualizar_multa/<int:pk>/", ActualizarMulta.as_view(), name='actualizar_multa'),
    path("vista_multa/<int:pk>/", VistaMulta.as_view(), name='vista_multa'),
    path("eliminar_multa/<int:pk>/", EliminarMulta.as_view(), name='eliminar_multa'),   
]   