from django.db import models 

#
from django.db.models import Q  #---> allows to use the syntax operator "or" 

#The function belong to exclusively for one model , in this case for autor.add()

class LibroManager(models.Manager):
    """ Managers for the model Autor """
    
    def listar_libros(self, kword):
        
        resultado = self.filter(
            titulo__icontains = kword  #---> Return the coincidences based on the attibute typed on kword
            )
        
        return resultado