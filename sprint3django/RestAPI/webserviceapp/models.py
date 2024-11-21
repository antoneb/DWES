# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tcomentarios(models.Model):
    comentario = models.CharField(max_length=2000, blank=True, null=True)
    libro = models.ForeignKey('Tlibros', models.DO_NOTHING)
    usuario = models.ForeignKey('Tusuarios', models.DO_NOTHING, blank=True, null=True)
    fechapost = models.DateTimeField(db_column='fechaPost', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tComentarios'


class Tlibros(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True)
    imagen = models.CharField(max_length=200, blank=True, null=True)
    anho = models.TextField(blank=True, null=True)  # This field type is a guess.
    genero = models.CharField(max_length=200, blank=True, null=True)
    autor = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tLibros'


class Tusuarios(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apell = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(unique=True, max_length=200, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=200, blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'tUsuarios'
