# Library Imports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import *
from datetime import datetime
from Ecop.domain.mascota import Mascota
from Ecop.application.Serializers.all_serializers import *
from django.db.models.functions import TruncDate
from django.db.models import Q


'''Use Case for List Pets to Doctor Panel for Date'''
@api_view(['GET'])
def agenda(request, fecha):
    fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
    mascota = Mascota.objects.annotate(fecha_consulta_date=TruncDate('fecha_consulta')).filter(fecha_consulta_date=fecha)
    mascotas_json = MascotaSerializer(mascota, many=True)
    if not mascota:
        return Response({'Message':'No existen mascotas programadas con esa fecha'}, status=HTTP_404_NOT_FOUND)
    else:
        return Response(mascotas_json.data, status=HTTP_200_OK)


'''Use Cases to Input search over list pets for Date'''
@api_view(['GET'])
def searchagenda(request, fecha, name):
    fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
    mascotas_data = []
    if not name:
        return Response({'Message':'Proporcione un nombre para buscar'}, status=HTTP_404_NOT_FOUND)
    else:
        mascota = Mascota.objects.annotate(fecha_consulta_date=TruncDate('fecha_consulta')).filter(
                                                                                (Q(fecha_consulta_date=fecha)) & 
                                                                                (Q(nombre_mascota__startswith=name)))
        mascota_json = MascotaSerializer(mascota, many= True).data
        if not mascota:
            tutor = Tutor.objects.filter(Q(nombre_tutor__startswith= name))
            if not tutor:
                return Response({'Message':'No existen mascotas programadas para hoy con esas caracteristicas'}, 
                                status=HTTP_404_NOT_FOUND)
            else:
                for t in tutor:
                    mascotas = Mascota.objects.annotate(fecha_consulta_date=TruncDate('fecha_consulta')).filter(
                                                                                (Q(fecha_consulta_date=fecha)) & 
                                                                                (Q(tutor=t)))         
                    mascotas_json = MascotaSerializer(mascotas, many=True).data
                    mascotas_data.append(mascotas_json)

                return Response({'Mascotas':mascotas_data}, status= HTTP_200_OK)
        else:
            mascotas_data.append(mascota_json)
            return Response({'Mascotas':mascotas_data},status=HTTP_200_OK)