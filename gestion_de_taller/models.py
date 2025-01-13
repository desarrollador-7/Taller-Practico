from django.db import models
from gestion_de_carros.models import Carro

class Taller(models.Model):
    """Clase modelo Taller para el registro de datos de una Taller.
    
    :param models: Administrar datos de un Taller
    :type models: Objeto
    :return: Una instancia de la clase Taller con los datos registrados
    :rtype: Taller
    """    
    
    idn = models.CharField(max_length=50, verbose_name = 'Id*') 
    nombre = models.CharField(max_length=50, verbose_name='Nombre*')
    direccion = models.CharField(max_length=50, verbose_name = 'Direccion*')
    telefono = models.IntegerField(verbose_name = 'Telefono*')
    especializacion = models.CharField(max_length=50, verbose_name = 'Especializacion*')
    
    class Meta:
        
        """Clase para la creacion de permisos
        """         
        
        default_permissions = ()
        permissions = (
            ('crear_taller', 'Puede Crear Un Taller'),
            ('vista_taller', 'Puede Consultar Taller'),
            ('actualizar_taller', 'Puede Actualizar datos del Taller'),
            ('eliminar_taller', 'Puede Eliminar un Taller'),  
        )
    
    def __str__(self):
        return  str(self.idn) + ' - ' + str(self.nombre)

class Mantenimiento(models.Model):
    """Clase modelo Mantenimiento para el registro de datos de un Mantenimiento para un carro.

    :param models: Administrar datos de un Mantenimiento.
    :type models: Objeto
    :return: Una instancia de la clase Mantenimiento con los datos registrados
    :rtype: Mantenimiento
    """    
    
    idn = models.CharField(max_length=50, verbose_name = 'Identificacion*')
    placa = models.ForeignKey(Carro, on_delete=models.PROTECT, verbose_name = 'Placa*')
    id_taller = models.ForeignKey(Taller, on_delete=models.PROTECT, verbose_name = 'Id Taller*')    
    fecha = models.DateTimeField(verbose_name = 'Fecha*')
    tipo_servicio = models.CharField(max_length=50, verbose_name = 'Tipo servicio*')
    costo = models.IntegerField(verbose_name = 'Costo*') 
    descripcion = models.TextField(verbose_name = 'Descripcion*')
    estado = models.BooleanField(verbose_name='¿Activo?', default=True)
    
    class Meta:
        """Clase para la creacion de permisos
        """         
        
        default_permissions = ()
        permissions = (
            ('crear_mantenimiento', 'Puede Crear Mantenimiento'),
            ('vista_mantenimiento', 'Puede Consultar Mantenimiento'),
            ('actualizar_mantenimiento', 'Puede Actualizar Mantenimiento'),
            ('eliminar_mantenimiento', 'Puede Eliminar Mantenimiento'),  
        )
    
    def __str__(self):
        return str(self.idn) + ' - ' + str(self.tipo_servicio) + ' - ' + str(self.descripcion)
    
    @staticmethod
    def listado_talleres():
        return Taller.objects.all()