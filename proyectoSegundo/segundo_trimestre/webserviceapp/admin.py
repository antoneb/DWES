from django.contrib import admin
from .models import *


# Register your models here.


class eventosExistentes(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'organizador', 'asistentes_maximos')
    search_fields = ('titulo',)


class usuariosExistentes(admin.ModelAdmin):
    list_display = ('first_name', 'tipo')
    search_fields = ('tipo',)


class reservasExistentes(admin.ModelAdmin):
    list_display = ('evento', 'usuario', 'entradas_reservadas')
    search_fields = ('tipo',)


class comentariosExistentes(admin.ModelAdmin):
    list_display = ('usuario', 'fechapost', 'evento', 'comentario')
    search_fields = ('',)


admin.site.register(Teventos, eventosExistentes)
admin.site.register(Tusuarios, usuariosExistentes)
admin.site.register(Treservas, reservasExistentes)
admin.site.register(Tcomentarios, comentariosExistentes)
