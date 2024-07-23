# Imports
from django.db import models
from .ecop import Ecop

class Autorizado(models.Model):
    nombre = models.CharField(max_length=300, null=True, blank= True, verbose_name='Nombre del Autorizado')
    dni = models.CharField(max_length=100, null=True, blank=True, verbose_name='Documento de Identidad')
    semestre = models.IntegerField(null=True, blank=True, verbose_name='Semestre del Estudiante')
    firma = models.ImageField(upload_to='firmas', blank=True)
    ecop = models.ForeignKey(Ecop, null= True, on_delete = models.SET_NULL)

    class Meta:
        db_table = 'autorizado'
        verbose_name = 'Autorizado'
        verbose_name_plural = 'Autorizados'

    def __str__(self) -> str:
        return self.nombre