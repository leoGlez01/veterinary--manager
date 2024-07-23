# Library Imports
from django.db import models
from .ecop import Ecop

'''Sistema Database Model'''
class Sistema(models.Model):
    sistema = models.CharField(max_length=80, null=True, blank=True, verbose_name='Nombre del Sistema')
    organo = models.CharField(max_length= 100, null=True, blank=True, verbose_name='Organo')
    enfermedad = models.CharField(max_length=100, null=True, blank=True, verbose_name='Enfermedad')
    observacion = models.TextField(max_length=500, null= True, blank=True, verbose_name='Observacion')
    ecop = models.ForeignKey(Ecop,null=False, blank=False, on_delete=models.CASCADE, verbose_name='Ecop')

    class Meta:
        db_table = 'sistema'
        managed = True
        verbose_name = 'Sistema'
        verbose_name_plural = 'Sistemas'

    def __str__(self):
        data = "{0} {1}"
        return data.format(self.sistema, self.enfermedad)
