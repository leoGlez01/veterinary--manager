# Imports
from django.db import models
from .tutor import Tutor

'''Mascota Database Model'''
class Mascota(models.Model):
    nombre_mascota = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nombre de la Mascota')
    especie = models.CharField(max_length=60, null=True, blank=True, verbose_name='Especie de la Mascota')
    raza = models.CharField(max_length=60, null=True, blank=True, verbose_name='Raza de la Mascota')
    edad = models.CharField(max_length=100, null=True, blank=True, verbose_name= 'Edad de la Mascota')
    color = models.CharField(max_length=50, null=True, blank=True, verbose_name='Color de la Mascota')
    sexo = models.CharField(max_length=20, null=True, blank=True, verbose_name='Sexo de la Mascota')
    chip = models.CharField(max_length=50, null=True, blank=True, verbose_name='Chip de la Mascota')
    tipo_consulta = models.TextField(max_length = 500, null=True, blank= True, verbose_name = 'Motivo de Consulta')
    observacion_urgencia = models.TextField(max_length = 500, null=True, blank= True, verbose_name = 'Observacion Urgencia')
    fecha_consulta = models.DateTimeField(verbose_name = 'Fecha de consulta')
    tutor = models.ForeignKey(Tutor, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Tutor de la mascota')


    class Meta:
        db_table = "mascota"
        managed = True
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"


    def __str__(self):
        data = "{0} {1} {2}"
        return data.format(self.nombre_mascota, self.especie, self.sexo)
