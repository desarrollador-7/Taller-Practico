from django.db import models

class Carro(models.Model):
    
    MARCA = (
        ('TOYOTA', 'Toyota'),
        ('FORD', 'Ford'),
        ('CHEVROLET', 'Chevrolet'),
        ('NISSAN', 'Nissan'),
        ('BMW', 'Bmw'),
    )
    
    marca = models.CharField(max_length=50, verbose_name='Marca*', choices=MARCA)
    modelo = models.CharField(max_length=50, verbose_name = 'Modelo*') 
    anio = models.DateTimeField(verbose_name = 'Fecha de creacion*')
    precio = models.IntegerField(verbose_name = 'Precio del carro*')
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
        return + ' - ' + str(self.marca) + ' - ' + str(self.modelo) + ' - ' + str(self.anio) + ' - ' + str(self.precio) + ' - ' + str(self.disponible) # no colocar todos los campos. 
    
    @staticmethod
    def listado_carros():
        return Carro.objects.all()