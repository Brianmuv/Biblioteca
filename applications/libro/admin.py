from django.contrib import admin

#imported local models:

from .models import Libro



# Register your models here.


admin.site.register(Libro)