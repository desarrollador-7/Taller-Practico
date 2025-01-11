from django.db import models

class Carro(models.Model):
    """Clase modelo Carro para el registro de datos de un carro.
    
    :param models: Administrar datos de un vehiculo
    :type models: Objeto
    :return: Una instancia de la clase Carro con los datos registrados
    :rtype: Carro
    """    
    
    MARCA = (
        ('TOYOTA', 'Toyota'),
        ('FORD', 'Ford'),
        ('CHEVROLET', 'Chevrolet'),
        ('NISSAN', 'Nissan'),
        ('BMW', 'Bmw'),
    )
    
    TIPO = (
        ('PRIVADO', 'Privado'),
        ('PUBLICO', 'Publico'),
    )
    
    placa = models.CharField(max_length=50, verbose_name = 'Placa*', blank=True, null=True) 
    marca = models.CharField(max_length=50, verbose_name='Marca*', choices=MARCA)
    modelo = models.CharField(max_length=50, verbose_name = 'Modelo*')
    anio = models.DateTimeField(verbose_name = 'Fecha de creacion*')
    color = models.CharField(max_length=50, verbose_name = 'Color*',  blank=True, null=True)
    tipo = models.CharField(max_length=50, verbose_name = 'Tipo*', choices=TIPO, blank=True, null=True) 
    precio = models.IntegerField(verbose_name = 'Precio del carro*')
    kilometraje = models.FloatField(max_length=50, verbose_name = 'Kilometraje*', blank=True, null=True) 
    disponible = models.BooleanField(verbose_name='¿Disponible?', default=True)
    
    
    class Meta:
        
        """Clase para la creacion de permisos
        """         
        
        default_permissions = ()
        permissions = (
            ('crear_carro', 'Puede Crear Carro'),
            ('ver_carro', 'Puede Consultar Carro'),
            ('actualizar_carros', 'Puede Actualizar Carro'),
            ('eliminar_carro', 'Puede Eliminar Carro'),  
        )
    
    def __str__(self):
        return  str(self.marca) + ' - ' + str(self.placa) + ' - ' + str(self.disponible)
    
    @staticmethod
    def listado_carros():
        return Carro.objects.all()