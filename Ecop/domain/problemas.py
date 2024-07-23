# Library Imports
from django.db import models
from .ecop import Ecop

'''Problema Database Model'''
class Problema(models.Model):
    problema = models.CharField(max_length=80, null=True, blank=True, verbose_name='Problema')
    maestra = models.CharField(max_length= 100, null=True, blank=True, verbose_name='Maestra')
    diagnostico_diferencial = models.TextField(max_length=500, null= True, blank=True, verbose_name='Diagnostico Diferencial')
    ecop = models.ForeignKey(Ecop,null=False, blank=False, on_delete=models.CASCADE, verbose_name='Ecop')

    class Meta:
        db_table = 'problema'
        managed = True
        verbose_name = 'Problema'
        verbose_name_plural = 'Problemas'

    def __str__(self):
        data = "{0} {1}"
        return data.format(self.problema, self.ecop)
