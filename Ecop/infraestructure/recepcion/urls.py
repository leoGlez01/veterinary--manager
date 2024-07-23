# Imports
from django.urls import path
from Ecop.application.UseCases.recepcion.register import *
from Ecop.application.UseCases.recepcion.filter import *
from Ecop.application.UseCases.recepcion.historias import obtener_historias

urlpatterns = [
    path('registrar/', registrar, name= 'registrar-mascota'),
    path('filtrar/tutor/<str:name>/', filtrar_tutores, name= 'filtrar-tutores'),
    path('filtrar/mascota/<int:pk>/', filtrar_mascota, name= 'filtrar-mascotas'),
    path('historia/<int:pk>/', obtener_historias, name= 'historia-clinica'),
]