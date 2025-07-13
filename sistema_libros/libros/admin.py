from django.contrib import admin
from django.contrib import admin
from .models import Libro

# Register your models here.


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "fecha_publicacion", "isbn")
    search_fields = ("titulo", "autor", "isbn")
    list_filter = ("fecha_publicacion",)
