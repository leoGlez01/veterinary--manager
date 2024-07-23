# Imports
from rest_framework.decorators import api_view
from rest_framework.status import *
from django.db.models import Q
from rest_framework.response import Response
from Ecop.domain.models import Tutor, Mascota
from Ecop.application.Serializers.all_serializers import *

'''Filter Views'''
@api_view(['GET'])
def filtrar_tutores(request, name):
    if not name:
        return Response({'Message':'No has proporcionado el nombre a buscar'},
                        status=HTTP_400_BAD_REQUEST)
    else:
        try:
            tutor = Tutor.objects.filter(Q(nombre_tutor__startswith= name))
            tutor_json = TutorSerializer(tutor, many=True)
            return Response(tutor_json.data,
                            status=HTTP_200_OK)
        except:
            return Response({'Message': 'No existen coincidencias en el sistema'},
                            status=HTTP_404_NOT_FOUND)

@api_view(['GET'])
def filtrar_mascota(request, pk):
    if pk == 0:
        return Response({'Message': 'No has proporcionado un id de tutor'},
                        status=HTTP_400_BAD_REQUEST)
    else:
        try:
            tutor_instance = Tutor.objects.get(id= pk)
            mascotas = Mascota.objects.filter(tutor = tutor_instance)
            mascota_json = MascotaSerializer(mascotas, many=True)
            return Response(mascota_json.data,
                            status=HTTP_200_OK)
        except:
            return Response({'Message': 'No existen mascotas relacionadas con el tutor proporcionado'},
                            status=HTTP_404_NOT_FOUND)