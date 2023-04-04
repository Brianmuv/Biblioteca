from django.shortcuts import render


#Generic views imported from Django
from django.views.generic import ListView


# Local models

from .models import Autor



# Create your views here.

class ListAutores(ListView):
    model = Autor
    context_object_name = 'lista_autores'
    template_name='autor/lista.html'
    
    def get_queryset(self):
        return Autor.objects.listar_autores()