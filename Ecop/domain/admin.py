from django.contrib import admin
from .models import *

admin.site.register((Tutor, Mascota, Ecop, Desparacitacion, Diagnostico, Mucosa, 
                     Nodulos, Problema, Sistema, Terapia, Vacunacion, Autorizado))
