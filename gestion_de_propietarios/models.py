from django.db import models
from gestion_de_carros.models import Carro

class Propietario(models.Model):
    
    dni = models.CharField(max_length=50, verbose_name = 'Identificacion*')
    placa = models.ForeignKey(Carro, on_delete=models.PROTECT, verbose_name = 'Placa*')   
    nombre = models.CharField(max_length=50, verbose_name = 'Nombre*')
    apellido = models.CharField(max_length=50, verbose_name = 'Apellido*')
    direccion = models.CharField(max_length=50, verbose_name = 'Direccion*')
    telefono = models.IntegerField(verbose_name = 'Telefono*') 
    email = models.EmailField(max_length=50, verbose_name = 'Email*')
    
    
    class Meta:
        """Clase para la creacion de permisos
        """         
        
        default_permissions = ()
        permissions = (
            ('crear_carro', 'Puede Crear Carros'),
            ('consultar_carros', 'Puede Consultar Carros'),
            ('editar_carros', 'Puede Editar Carros'),
            ('eliminar_carros', 'Puede Eliminar Carros'),  
        )
    
    def __str__(self):
        return str(self.dni) + ' - ' + str(self.email) + ' - ' + str(self.placa.placa)
    
    def mostrar_placa(self):
        return str(self.placa.placa)
    
    @staticmethod
    def listado_propietarios():
        return Propietario.objects.all()