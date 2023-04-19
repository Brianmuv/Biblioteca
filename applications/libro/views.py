from django.shortcuts import render


#Generic views imported from Django
from django.views.generic import ListView


# Local models

from .models import Libro



# Create your views here.

class ListLibro(ListView):
    model = Libro
    context_object_name = 'lista_libros'
    template_name='libro/lista.html'
    
    def get_queryset(self):
        key_word = self.request.GET.get('kword', '')  #---> Intercep the GET method by keyword set on html "kword"
        
        return Libro.objects.listar_libros(key_word)