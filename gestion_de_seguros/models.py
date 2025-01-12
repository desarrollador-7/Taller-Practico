from django.db import models
from gestion_de_carros.models import Carro

class Aseguradora(models.Model):
    """Clase modelo Aseguradora para el registro de datos de una Aseguradora.
    
    :param models: Administrar datos de una Aseguradora
    :type models: Objeto
    :return: Una instancia de la clase Aseguradora con los datos registrados
    :rtype: Aseguradora
    """    
    
    id_aseguradora = models.CharField(max_length=50, verbose_name = 'Id*') 
    nombre = models.CharField(max_length=50, verbose_name='Nombre*')
    direccion = models.CharField(max_length=50, verbose_name = 'Direccion*')
    telefono = models.IntegerField(verbose_name = 'Telefono*')
    email = models.EmailField(max_length=50, verbose_name = 'Email*')
    
    class Meta:
        
        """Clase para la creacion de permisos
        """         
        
        default_permissions = ()
        permissions = (
            ('crear_aseguradora', 'Puede Crear Una Aseguradora'),
            ('vista_aseguradora', 'Puede Consultar Aseguradora'),
            ('actualizar_aseguradora', 'Puede Actualizar una Aseguradora'),
            ('eliminar_aseguradora', 'Puede Eliminar una Aseguradora'),  
        )
    
    def __str__(self):
        return  str(self.id) + ' - ' + str(self.nombre)


class Seguro(models.Model):
    """Clase modelo Seguro para el registro de datos de un Seguro.

    :param models: Administrar datos de un Seguro.
    :type models: Objeto
    :return: Una instancia de la clase Seguro con los datos registrados
    :rtype: Seguro
    """    
    
    dni = models.CharField(max_length=50, verbose_name = 'Identificacion*')
    placa = models.ForeignKey(Carro, on_delete=models.PROTECT, verbose_name = 'Placa*')
    id_aseguradora = models.ForeignKey(Aseguradora, on_delete=models.PROTECT, verbose_name = 'Id aseguradora*')    
    fecha_inicio = models.DateTimeField(verbose_name = 'Fecha Inicio*')
    fecha_fin = models.DateTimeField(verbose_name = 'Fecha Fin*')
    costo = models.CharField(max_length=50, verbose_name = 'Costo*')
    tipo_cobertura = models.IntegerField(verbose_name = 'Cobertura*') 
    estado = models.BooleanField(verbose_name='¿Activo?', default=True)
    
    class Meta:
        """Clase para la creacion de permisos
        """         
        
        default_permissions = ()
        permissions = (
            ('crear_seguro', 'Puede Crear Seguro'),
            ('vista_seguro', 'Puede Consultar Seguro'),
            ('actualizar_seguro', 'Puede Actualizar Seguro'),
            ('eliminar_seguro', 'Puede Eliminar Seguro'),  
        )
    
    def __str__(self):
        return str(self.id_aseguradora.id_aseguradora)
    
    @staticmethod
    def listado_aseguradoras():
        return Aseguradora.objects.all()