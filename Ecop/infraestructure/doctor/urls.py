# Imports
from django.urls import path
from Ecop.application.UseCases.doctor.consulta import *
from Ecop.application.UseCases.doctor.list_pets import *
from Ecop.application.UseCases.recepcion.historias import *
from Ecop.application.UseCases.doctor.list_pday import *

urlpatterns = [
    path('ecop/', createEcop, name= 'create-ecop'),
    path('agenda/<str:fecha>/', agenda, name= 'agenda'),
    path('listpday/<str:fecha>/', list_pday, name= 'list-day'),
    path('searchagenda/<str:fecha>/<str:name>/', searchagenda, name= 'search-agenda'),
]