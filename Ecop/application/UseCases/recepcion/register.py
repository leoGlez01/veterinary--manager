# Library imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
from Ecop.domain.models import Tutor, Mascota
from Ecop.application.Serializers.all_serializers import *


'''Use Case for register from Reception View'''
@api_view(['POST'])
def registrar(request):
    data = request.data
    tutor_data = {
        'nombre_tutor': data['nombre_tutor'],
        'dni': data['dni'],
        'telefono': data['telefono'],
        'direccion':data['direccion']
    }

    tutor_comparacion = Tutor.objects.filter(dni= data['dni'])
    if tutor_comparacion.exists():
        tutor_instance = tutor_comparacion.first()
    else:
        tutor_instance = Tutor.objects.create(**tutor_data)
    
    tutor_json = TutorSerializer(tutor_instance, many=False)
    mascotas_data = data['mascotas']
    mascotas_json = []

    for mascota_data in mascotas_data:
        mascota_instance = Mascota.objects.create(tutor= tutor_instance, **mascota_data)
        mascota_json = MascotaSerializer(mascota_instance, many=False)
        mascotas_json.append(mascota_json.data)

    return Response({
        'Message': 'Todo empingao!!!',
        'tutor': tutor_json.data,
        'mascotas': mascotas_json
        }, status=HTTP_201_CREATED)

