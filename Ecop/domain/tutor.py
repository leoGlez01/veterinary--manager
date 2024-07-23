# Imports
from django.db import models

'''Tutor Database Model'''
class Tutor(models.Model):
    nombre_tutor = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nombre del Tutor')
    dni = models.CharField(max_length=100, null=True, blank=True, verbose_name='Identidad del Tutor')
    direccion = models.CharField(max_length= 300, null = True, blank = True, verbose_name= 'Direccion del Tutor')
    telefono = models.CharField(max_length=20, null=True, blank=True, verbose_name='Contacto del Tutor')

    class Meta:
        db_table = 'tutor'
        managed = True
        verbose_name = 'Tutor'
        verbose_name_plural = 'Tutores'

    def __str__(self):
        data = "{0} {1}"
        return data.format(self.nombre_tutor, self.dni)