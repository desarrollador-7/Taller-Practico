from django.db import models

class Carro(models.Model):
    
    MARCA = (
        ('TOYOTA', 'Toyota'),
        ('FORD', 'Ford'),
        ('CHEVROLET', 'Chevrolet'),
        ('NISSAN', 'Nissan'),
        ('BMW', 'Bmw'),
    )
    
    placa = models.CharField(max_length=50, verbose_name = 'Placa*', blank=True, null=True) 
    marca = models.CharField(max_length=50, verbose_name='Marca*', choices=MARCA)
    modelo = models.CharField(max_length=50, verbose_name = 'Modelo*') 
    anio = models.DateTimeField(verbose_name = 'Fecha de creacion*')
    color = models.CharField(max_length=50, verbose_name = 'Color*', blank=True, null=True) 
    tipo = models.CharField(max_length=50, verbose_name = 'Tipo*', blank=True, null=True) 
    precio = models.IntegerField(verbose_name = 'Precio del carro*')
    kilometraje = models.FloatField(max_length=50, verbose_name = 'Kilometraje*', blank=True, null=True) 
    disponible = models.BooleanField(verbose_name='¿Disponible?', default=True)
    
    
    class Meta: 
        default_permissions = ()
        permissions = (
            ('crear_carro', 'Puede Crear Carros'),
            ('consultar_carros', 'Puede Consultar Carros'),
            ('editar_carros', 'Puede Editar Carros'),
            ('eliminar_carros', 'Puede Eliminar Carros'),  
        )
    
    def __str__(self):
        return + ' - ' + str(self.marca) + ' - ' + str(self.modelo) + ' - ' + str(self.disponible)
    
    @staticmethod
    def listado_carros():
        return Carro.objects.all()