from django.db import models 


#The function belong to exclusively for one model , in this case for autor.add()

class AutorManager(models.Manager):
    """ Managers for the model Autor """
    
    def listar_autores(self):
        return self.all()