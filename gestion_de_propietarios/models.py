from django.db import models
from gestion_de_carros.models import Carro
class Propietario(models.Model):
    """Clase modelo Propietario para el registro de datos de un carro.

    :param models: Abministrar datos de propietarios.
    :type models: Objeto
    :return: Una instancia de la clase Propietario con los datos registrados
    :rtype: Propietario
    """    
    
    dni = models.CharField(max_length=50, verbose_name = 'Identificacion*')
    placa = models.ForeignKey(Carro, on_delete=models.PROTECT, verbose_name = 'Placa*')   
    nombre = models.CharField(max_length=50, verbose_name = 'Nombre*')
    apellido = models.CharField(max_length=50, verbose_name = 'Apellido*')
    direccion = models.CharField(max_length=50, verbose_name = 'Direccion*')
    telefono = models.CharField(verbose_name='Telefono*', max_length=20)
    email = models.EmailField(max_length=50, verbose_name = 'Email*')
    
    class Meta:
        """Clase para la creacion de permisos
        """         
        
        default_permissions = ()
        permissions = (
            ('crear_propietario', 'Puede Crear Propietarios'),
            ('vista_propietario', 'Puede Consultar Propietarios'),
            ('actualizar_propietario', 'Puede Actualizar Propietarios'),
            ('eliminar_propietario', 'Puede Eliminar Propietarios'),  
        )
    
    def __str__(self):
        return self.nombre

class Licencia(models.Model):
    """Clase modelo Licencia para el registro de datos de un Propietario.

    :param models: Abministrar datos de licencias.
    :type models: Objeto
    :return: Una instancia de la clase Licencia con los datos registrados
    :rtype: Licencia
    """    
    
    TIPO = (
        ('PRIVADO', 'Privado'),
        ('PUBLICO', 'Publico'),
    )
    
    numero = models.CharField(max_length=50, verbose_name = 'N.Licencia*')
    dni = models.ForeignKey(Propietario, on_delete=models.PROTECT, verbose_name = 'Identificacion*')   
    tipo = models.CharField(max_length=50, verbose_name = 'Tipo*', choices=TIPO)
    fecha_emision = models.DateTimeField(verbose_name = 'Fecha de emision*')
    fecha_vencimiento = models.DateTimeField(verbose_name = 'Fecha de vencimiento*')
    estado = models.BooleanField(verbose_name='¿Activo?', default=True)
    
    
    class Meta:
        """Clase para la creacion de permisos
        """         
        
        default_permissions = ()
        permissions = (
            ('crear_licencia', 'Puede Crear licencia'),
            ('ver_licencia', 'Puede Consultar Licencias'),
            ('actualizar_licencia', 'Puede Actualizar Licencia'),
            ('eliminar_licencia', 'Puede Eliminar Licencia'),  
        )
        
    def __str__(self):
        return str(self.dni.dni) + ' - ' + str(self.estado)
    
    @staticmethod
    def listado_propietarios():
        return Propietario.objects.all()