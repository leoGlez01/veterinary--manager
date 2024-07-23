# Library Imports
from django.db import models
from .ecop import Ecop


'''Terapia Database Model'''
class Terapia(models.Model):
    tratamiento = models.CharField(max_length=100, null=True, blank=True, verbose_name='Tratamiento')
    principio_activo = models.CharField(max_length=100, null=True, blank=True, verbose_name='Principio Activo')
    presentacion = models.CharField(max_length=100, null=True, blank=True, verbose_name='Presentacion')
    posologia = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Posologia')
    dosis_total = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Dosis Total')
    via = models.CharField(max_length=100, null=True, blank=True, verbose_name='Via de Tratamiento')
    frecuencia = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Frecuencia de Tratamiento')
    duracion = models.CharField(max_length=100, null=True, blank=True, verbose_name='Duracion del Tratamiento')
    ecop = models.ForeignKey(Ecop, null= False, blank= False, on_delete= models.CASCADE, verbose_name= 'Ecop')

    class Meta:
        db_table = 'terapia'
        managed = True
        verbose_name = 'Terapia'
        verbose_name_plural = 'Terapias'

    def __str__(self):
        data = "{0} {1}"
        return data.format(self.tratamiento, self.principio_activo)