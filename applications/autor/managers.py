from django.db import models 

#
from django.db.models import Q  #---> allows to use the syntax operator "or" 

#The function belong to exclusively for one model , in this case for autor.add()

class AutorManager(models.Manager):
    """ Managers for the model Autor """
    
    def buscar_autor(self, kword):
        
        resultado = self.filter(
            nombre__icontains = kword  #---> Return the coincidences based on the attibute typed on kword
            )
        
        return resultado
    
    
    # OR operator
    
    def buscar_autor2(self, kword):
        
        resultado = self.filter(
             Q(nombre__icontains = kword) | Q(apellidos__icontains = kword)#---> Return the coincidences based on the attibute typed on kword
        
        )
        
        return resultado
    
    # exclude()
    
    def buscar_autor3(self, kword):
        
        resultado = self.filter(
             nombre__icontains = kword  #---> Return the coincidences based on the attibute typed on kword
        
        ).exclude(edad = 58)
        
        return resultado
    
    # Higher(gt) or lower(lt):
    
    def buscar_autor4(self, kword):
        resultado = self.filter(
                edad__gt = 40,  #---> Higher
                edad__lt = 65   #---> lower    ---> Return ages between 40 or 65
        ).order_by('apellidos')   #---> order based on lastname, we could add more attributes to order. 
        return resultado
    
    