# Imports
from rest_framework.response import Response
from Ecop.domain.models import Vacunacion, Desparacitacion
from Ecop.application.Serializers.all_serializers import VacunacionSerializer, DesparacitacionSerializer,DiagnosticoSerializer
from rest_framework.decorators import api_view
from datetime import datetime
from rest_framework.status import HTTP_200_OK

@api_view(['GET'])
def list_pday(request, fecha):
    fecha_obj = datetime.strptime(fecha, "%Y-%m-%d").date()
    vacunaciones = Vacunacion.objects.filter(fecha=fecha_obj)
    desparacitaciones = Desparacitacion.objects.filter(fecha= fecha_obj)
    vacunacion_json = VacunacionSerializer(vacunaciones, many=True).data
    desparacitacion_json = DesparacitacionSerializer(desparacitaciones, many=True).data

    
    vacunaciones_json= [vacunacion_json]
    desparacitaciones_json= [desparacitacion_json]

    return Response({'vacunaciones':vacunaciones_json,
                     'desparacitaciones':desparacitaciones_json
                     },status=HTTP_200_OK)