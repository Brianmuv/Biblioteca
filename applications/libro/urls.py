from django.contrib import admin
from django.urls import path

#local seting imports:

from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path(
        'libros/', 
        views.ListLibro.as_view(),
         name="libros"),
]
