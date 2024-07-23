# Imports
from django.db import models
from .mascota import Mascota


'''Ecop DB Model'''
class Ecop(models.Model):
    anamnesis = models.TextField(max_length= 800, null = True, verbose_name = 'Anamnesis')
    motivo_consulta = models.TextField(max_length = 500, null=True, blank= True, verbose_name = 'Motivo de Consulta')
    alergias = models.TextField(max_length= 800, null= True, verbose_name= 'Alergias')
    enfermedades_anteriores = models.TextField(max_length= 800, null= True, verbose_name= 'Enfermedades Anteriores')
    antescedentes_familiares = models.TextField(max_length= 800, null= True, verbose_name= 'Antescedentes Familiares')
    cirugias = models.TextField(max_length= 800, null= True, verbose_name= 'Cirugia')
    estado_reproductivo = models.CharField(max_length= 150, null= True, verbose_name= 'Estado Reproductivo')
    alimentacion = models.CharField(max_length= 150, null= True, verbose_name= 'Alimentacion')
    habitat = models.CharField(max_length= 150, null= True, verbose_name= 'Habitat')
    tllc = models.DecimalField(max_digits= 6, decimal_places= 2, null= True, verbose_name= 'TLLC')
    pulso = models.DecimalField(max_digits= 6, decimal_places= 2, null= True, verbose_name= 'Pulso')
    fc = models.DecimalField(max_digits= 6, decimal_places= 2, null= True, verbose_name= 'FC')
    fr = models.DecimalField(max_digits= 6, decimal_places= 2, null= True, verbose_name= 'FR')
    temperatura = models.DecimalField(max_digits= 6, decimal_places= 2, null= True, verbose_name= 'Temperatura')
    peso = models.DecimalField(max_digits= 6, decimal_places= 2, null= True, verbose_name= 'Peso')
    actitud = models.CharField(max_length= 150, null= True, verbose_name= 'Actitud')
    condicion_corporal = models.CharField(max_length= 150, null= True, verbose_name= 'Condicion Corporal')
    hidratacion = models.CharField(max_length= 150, null= True, verbose_name= 'Hidratacion')
    interpretacion_resultados = models.TextField(max_length=500, null= True, blank=True, verbose_name='Interpretacion Resultados')
    impresion_diagnostica = models.TextField(max_length=500, null= True, blank=True, verbose_name='Impresion Diagnostico')
    estado = models.CharField(max_length = 20, null=True, blank= True, verbose_name = 'Estado de la mascota')
    mascota = models.ForeignKey(Mascota, null= False, on_delete = models.CASCADE)
    
    class Meta:
        db_table = "ecop"
        managed = True
        verbose_name = "Ecop"
        verbose_name_plural = "Ecops"


    def __str__(self) -> str:
        return self.motivo_consulta