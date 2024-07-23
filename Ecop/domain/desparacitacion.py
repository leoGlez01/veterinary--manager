# Library Imports
from django.db import models
from .ecop import Ecop

'''Desparacitacion Database Model'''
class Desparacitacion(models.Model):
    producto = models.CharField(max_length=100, null=True, blank=True, verbose_name='Producto')
    fecha = models.DateField(verbose_name='Fecha de Desparacitacion')
    ecop = models.ForeignKey(Ecop, null= False, blank= False, on_delete=models.CASCADE, verbose_name= 'Ecop')

    class Meta:
        db_table = 'desparacitacion'
        managed = True
        verbose_name = 'Desparacitacion'
        verbose_name_plural = 'Desparacitaciones'

    def __str__(self):
        data = "{0} {1}"
        return data.format(self.producto, self.fecha)
