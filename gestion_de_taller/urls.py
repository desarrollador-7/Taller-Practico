from django.urls import path
from .views import *

urlpatterns = [
    ####--------Taller--------####
    path("listado_talleres", ListaTaller.as_view(), name='listado_talleres'),
    path("crear_taller", CrearTaller.as_view(), name='crear_taller'),
    path("actualizar_taller/<int:pk>/", ActualizarTaller.as_view(), name='actualizar_taller'),
    path("vista_taller/<int:pk>/", VistaTaller.as_view(), name='vista_taller'),
    path("eliminar_taller/<int:pk>/", EliminarTaller.as_view(), name='eliminar_taller'),   
    
    ####--------Mantenimiento--------####
    path("listado_mantenimientos", ListaMantenimiento.as_view(), name='listado_mantenimientos'),
    path("crear_mantenimiento", CrearMantenimiento.as_view(), name='crear_mantenimiento'),
    path("actualizar_mantenimiento/<int:pk>/", ActualizarMantenimiento.as_view(), name='actualizar_mantenimiento'),
    path("vista_mantenimiento/<int:pk>/", VistaMantenimiento.as_view(), name='vista_mantenimiento'),
    path("eliminar_mantenimiento/<int:pk>/", EliminarMantenimiento.as_view(), name='eliminar_mantenimiento'), 
]