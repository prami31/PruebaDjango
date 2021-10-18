from django.contrib import admin

from core.models import Autor, Libro, Receta


class LibroInline(admin.TabularInline):
    model = Libro


class RecetaInline(admin.TabularInline):
    model = Receta


class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombres', 'apellidos', 'ciudad']
    list_filter = ['ciudad']
    search_fields = ['nombres', 'apellidos']
    inlines = [LibroInline, RecetaInline]


admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro)
