import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Tusuarios(AbstractUser):
    biografia = models.TextField()
    TIPO_USUARIO = [
        ('organizador', 'Organizador'),
        ('asistente', 'Asistente')
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_USUARIO, default='asistente')

    def __str__(self):
        return self.first_name

class Teventos(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True)
    imagen = models.CharField(max_length=200, blank=True, null=True)
    calendario = models.DateTimeField(db_column='calendario_evento', blank=True, null=True, default=datetime.now())
    asistentes_maximos = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField()
    organizador = models.ForeignKey('Tusuarios', models.DO_NOTHING)

    def __str__(self):
        return "[" + self.organizador.first_name + "] " + self.titulo


class Tcomentarios(models.Model):
    comentario = models.CharField(max_length=2000, blank=True, null=True)
    evento = models.ForeignKey('Teventos', models.DO_NOTHING)
    usuario = models.ForeignKey('Tusuarios', models.DO_NOTHING)
    fechapost = models.DateTimeField(db_column='fecha_comentario', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return "[" + self.usuario.first_name + "] [" + self.evento.titulo + "] " + self.comentario


class Treservas(models.Model):
    evento = models.ForeignKey('Teventos', models.DO_NOTHING)
    usuario = models.ForeignKey('Tusuarios', models.DO_NOTHING, )
    entradas_reservadas = models.IntegerField()
    TIPO_RESERVA = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'cancelada')
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_RESERVA, default='pendiente')

    def __str__(self):
        return self.evento.titulo
