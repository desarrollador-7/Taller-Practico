from django.urls import path
from .views import *

urlpatterns = [
    ####--------Aseguradora--------####
    path("listado_aseguradoras", ListaAseguradora.as_view(), name='listado_aseguradoras'),
    path("crear_aseguradora", CrearAseguradora.as_view(), name='crear_aseguradora'),
    path("actualizar_aseguradora/<int:pk>/", ActualizarAseguradora.as_view(), name='actualizar_aseguradora'),
    path("vista_aseguradora/<int:pk>/", VistaAseguradora.as_view(), name='vista_aseguradora'),
    path("eliminar_aseguradora/<int:pk>/", EliminarAseguradora.as_view(), name='eliminar_aseguradora'),   
    
    ####--------Seguros--------####
    path("listado_seguros", ListaSeguros.as_view(), name='listado_seguros'),
    path("crear_seguro", CrearSeguro.as_view(), name='crear_seguro'),
    path("actualizar_seguro/<int:pk>/", ActualizarSeguro.as_view(), name='actualizar_seguro'),
    path("vista_seguro/<int:pk>/", VistaSeguro.as_view(), name='vista_seguro'),
    path("eliminar_seguro/<int:pk>/", EliminarSeguro.as_view(), name='eliminar_seguro'), 
]