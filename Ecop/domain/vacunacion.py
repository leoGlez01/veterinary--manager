# Imports
from django.db import models
from .ecop import Ecop


class Vacunacion(models.Model):
    tipo_vacuna = models.CharField(max_length = 150, null= True, verbose_name= 'Tipo de vacunacion')
    producto = models.CharField(max_length = 150, null= True, verbose_name= 'Producto')
    fecha = models.DateField(verbose_name = 'Fecha de Vacunacion')
    ecop = models.ForeignKey(Ecop, null= False, on_delete= models.CASCADE, verbose_name= 'Ecop')
    

    class Meta:
        db_table = 'vacunacion'
        verbose_name = 'Vacunacion'
        verbose_name_plural = 'Vacunaciones'
        managed = True


    def __str__(self) -> str:
        data = "{0}: {1}"
        return data.format(self.tipo_vacuna, self.ecop)