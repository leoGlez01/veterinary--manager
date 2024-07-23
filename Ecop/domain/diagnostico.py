# Library Imports
from django.db import models
from .ecop import Ecop

'''Diagnostico Database Model'''
class Diagnostico(models.Model):
    tipo_examen = models.CharField(max_length=80, null=True, blank=True, verbose_name='Diagnostico')
    autorizado = models.CharField(max_length= 100, null=True, blank=True, verbose_name='Autorizacion')
    laboratorio = models.CharField(max_length=100, null=True, blank=True, verbose_name='Laboratorio')
    resultados = models.TextField(max_length=500, null= True, blank=True, verbose_name='Resultados')
    fecha = models.DateField(verbose_name = 'Fecha del Diagnostico')
    ecop = models.ForeignKey(Ecop,null=False, blank=False, on_delete=models.CASCADE, verbose_name='Ecop')

    class Meta:
        db_table = 'diagnostico'
        managed = True
        verbose_name = 'Diagnostico'
        verbose_name_plural = 'Diagnosticos'

    def __str__(self):
        data = "{0} {1}"
        return data.format(self.tipo_examen, self.ecop)
