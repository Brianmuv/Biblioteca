from django.contrib import admin



#imported local models:

from .models import Autor

# Register your models here.

admin.site.register(Autor)