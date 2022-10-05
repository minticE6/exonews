from django.db import models
 
class explanetas (models.Model): # para datos curiosos de exoplanetas extraidos desde wikipedia
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre' )
    tipo = models.CharField(max_length=100, verbose_name='Tipo')
    distancia = models.CharField(max_length=100, verbose_name='Distancia')
    descubrimiento = models.CharField(max_length=100, verbose_name='Descubrimiento' )
    constelacion = models.CharField(max_length=100, verbose_name='Constelación')
    def __self__(self):
        fila = "Nombre_" + self.nombre + '-' + "Descubrimiento" + self.descubrimiento
        return fila
    
class userandpassword(models.Model): #conexion de datos entre el HTML y el backend y la base de datos
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    correo = models.CharField(max_length=100, verbose_name='Correo')
    apodo = models.CharField(max_length=100, verbose_name='Apodo')
    def __self__(self):
        fila = "Nombre_" + self.nombre + "_" + "Apellido" + self.apellido + "-" + "Apodo" + self.apodo
        return fila
    
    