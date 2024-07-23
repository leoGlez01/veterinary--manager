# Library Imports
from django.db import models
from .ecop import Ecop

'''Nodulos Database Model'''
class Nodulos(models.Model):
    estado = models.BooleanField(default=True, null=True, blank=True, verbose_name='Estado')
    observacion_nodulos = models.TextField(max_length=300, null=True, blank=True, verbose_name='Observacion')
    ecop = models.ForeignKey(Ecop, null=False, blank=False, on_delete=models.CASCADE, verbose_name='Ecop')

    class Meta:
        db_table = 'nodulos'
        managed = True
        verbose_name = 'Nodulos'
        verbose_name_plural = 'Nodulos'

    def __str__(self):
        data = "{0} {1}"
        return data.format(self.estado, self.ecop)