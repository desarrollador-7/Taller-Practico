from django.db import models
from gestion_de_carros.models import Carro

class Multas(models.Model):
    """Clase modelo Multas para el registro de datos de las multas.
    
    :param models: Administrar datos de las multas
    :type models: Objeto
    :return: Una instancia de la clase Multa con los datos registrados
    :rtype: Multa
    """  
    
    id = models.CharField(max_length=50, verbose_name = 'Id*') 
    placa = models.ForeignKey(Carro, on_delete=models.PROTECT, verbose_name = 'Placa*')
    fecha = models.DateTimeField(verbose_name = 'Fecha*')
    infraccion = models.PositiveIntegerField(verbose_name = 'Infraccion*')
    monto = models.PositiveIntegerField(verbose_name = 'Monto*')
    estado = models.BooleanField(verbose_name='¿Activo?', default=True) 
    
    class Meta:
        
        """Clase para la creacion de permisos
        """         
        
        default_permissions = ()
        permissions = (
            ('crear_multa', 'Puede Crear Multas'),
            ('ver_multa', 'Puede Consultar Multas'),
            ('actualizar_multa', 'Puede Actualizar Multa'),
            ('eliminar_multa', 'Puede Eliminar Multa'),  
        )
    
    def __str__(self):
        return  str(self.id) + ' - ' + str(self.placa.placa) + ' - ' + str(self.estado)
    
    @staticmethod
    def listado_multas():
        return Multas.objects.all()