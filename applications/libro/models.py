from django.db import models



#Imports for tables:
from applications.autor.models import Autor 


# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
    

class Libro(models.Model):
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField('Fecha de Lanzamiento')
    portada = models.ImageField(upload_to='portada', height_field=None, width_field=None, max_length=None)
    visitas = models.PositiveIntegerField()
    
    def __str__(self):
        return self.titulo
    
    