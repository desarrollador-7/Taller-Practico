from django.urls import path
from .views import *

urlpatterns = [
    ####--------Propietario--------####
    path("listado_propietarios", ListaPropietario.as_view(), name='listado_propietarios'),
    path("crear_propietario", CrearPropietario.as_view(), name='crear_propietario'),
    path("actualizar_propietario/<int:pk>/", ActualizarPropietario.as_view(), name='actualizar_propietario'),
    path("vista_propietario/<int:pk>/", VistaPropietario.as_view(), name='vista_propietario'),
    path("eliminar_propietario/<int:pk>/", EliminarPropietario.as_view(), name='eliminar_propietario'),  
    
    ####--------Licencia--------#### 
    path("listado_licencias", ListaLicencia.as_view(), name='listado_licencias'),
    path("crear_licencia", CrearLicencia.as_view(), name='crear_licencia'),
    path("actualizar_licencia/<int:pk>/", ActualizarLicencia.as_view(), name='actualizar_licencia'),
    path("vista_licencia/<int:pk>/", VistaLicencia.as_view(), name='vista_licencia'),
    path("eliminar_licencia/<int:pk>/", EliminarLicencia.as_view(), name='eliminar_licencia'),
]