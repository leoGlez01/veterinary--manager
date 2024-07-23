# Library Imports
from django.db import models
from .ecop import Ecop

'''Mucosa Database Model'''
class Mucosa(models.Model):
    rectal = models.BooleanField(default=True, null=True, blank=True, verbose_name='Mucosa Rectal')
    conjuntival = models.BooleanField(default=True, null=True, blank=True, verbose_name='Mucosa Conjuntival')
    vulvar_prepucial = models.BooleanField(default=True, null=True, blank=True, verbose_name='Mucosa Vulvar o Prepucial')
    observacion_rectal = models.TextField(max_length=300, null=True, blank=True, verbose_name='Observacion')
    observacion_conjuntival = models.TextField(max_length=300, null=True, blank=True, verbose_name='Observacion')
    observacion_vulvar_prepucial = models.TextField(max_length=300, null=True, blank=True, verbose_name='Observacion')
    ecop = models.ForeignKey(Ecop, null=False, blank=False, on_delete=models.CASCADE, verbose_name='Ecop')

    class Meta:
        db_table = 'mucosa'
        managed = True
        verbose_name = 'Mucosa'
        verbose_name_plural = 'Mucosas'

    def __str__(self):
        return self.observacion_rectal