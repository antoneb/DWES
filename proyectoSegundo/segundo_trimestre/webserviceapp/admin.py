from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Tcomentarios)

class eventosExistentes(admin.ModelAdmin):
    list_display = ('titulo','descripcion','organizador','asistentes_maximos')
    search_fields = ('titulo',)

class usuariosExistentes(admin.ModelAdmin):
    list_display = ('first_name','tipo')
    search_fields = ('tipo',)

class reservasExistentes(admin.ModelAdmin):
    list_display = ('evento','usuario','entradas_reservadas')
    search_fields = ('tipo',)

admin.site.register(Teventos, eventosExistentes)
admin.site.register(Tusuarios, usuariosExistentes)
admin.site.register(Treservas,reservasExistentes)