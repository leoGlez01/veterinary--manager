# Imports
from Ecop.domain.models import *
from Ecop.application.Serializers.all_serializers import *
from rest_framework.status import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime


'''Function to create ECOP instance for each pet'''
@api_view(['POST'])
def createEcop(request):
    data = request.data
    mascota_id = data['mascota_id']
    if not mascota_id:
        return Response({'Message':'Algo salio mal en la peticion. No se esta enviando el id de la mascota!'},
                        status=HTTP_400_BAD_REQUEST)
    else:
        mascota_instance = Mascota.objects.get(id = mascota_id)
        sistemas_data = data['sistemas']
        problemas_data = data['problemas']
        diagnosticos_data = data['diagnosticos']
        terapias_data = data['planes_terapeuticos']
        autorizados_data = data['pasantes']
        mucosas_data = data['mucosas']
        nodulos_data = data['nodulos']
        desparacitaciones_data = data['desparacitaciones']
        vacunaciones_data = data['vacunaciones']

        ecop_data = data['ecop']
        ecop_instance = Ecop.objects.create(mascota=mascota_instance, **ecop_data)
        ecop_json = EcopSerializer(ecop_instance, many= False)

        for sistema in sistemas_data:
            sistema_instance = Sistema.objects.create(ecop = ecop_instance, **sistema)
            sistema_json = SistemaSerializer(sistema_instance, many= False)

        for problema in problemas_data:
            problema_instance = Problema.objects.create(ecop = ecop_instance, **problema)
            problema_json = ProblemaSerializer(problema_instance, many= False)

        for diagnostico in diagnosticos_data:
            fecha_del_request_diag = diagnostico.get('fecha')
            fecha_convertida = datetime.datetime.strptime(fecha_del_request_diag, "%Y-%m-%d").date()
            del diagnostico['fecha']
            diagnostico['fecha'] = fecha_convertida
            diagnostico_instance = Diagnostico.objects.create(ecop= ecop_instance, **diagnostico)
            diagnostico_json = DiagnosticoSerializer(diagnostico_instance, many= False)

        for terapia in terapias_data:
            terapia_instance = Terapia.objects.create(ecop = ecop_instance, **terapia)
            terapia_json = TerapiaSerializer(terapia_instance, many= False)

        for autorizado in autorizados_data:
            autorizado_instance = Autorizado.objects.create(ecop = ecop_instance, **autorizado)
            autorizado_json = AutorizadoSerializer(autorizado_instance, many= False)

        fecha_del_request_des = desparacitaciones_data.get('fecha')
        fecha_convertida = datetime.datetime.strptime(fecha_del_request_des, "%Y-%m-%d").date()
        del desparacitaciones_data['fecha']
        desparacitaciones_data['fecha'] = fecha_convertida
        desparacitacion_instance = Desparacitacion.objects.create(ecop=ecop_instance, **desparacitaciones_data)
        desparacitacion_json = DesparacitacionSerializer(desparacitacion_instance, many= False)

        fecha_del_request_vac = vacunaciones_data.get('fecha')
        fecha_convertida = datetime.datetime.strptime(fecha_del_request_vac, "%Y-%m-%d").date()
        del vacunaciones_data['fecha']
        vacunaciones_data['fecha'] = fecha_convertida
        vacunacion_instance = Vacunacion.objects.create(ecop=ecop_instance, **vacunaciones_data)
        vacunacion_json = VacunacionSerializer(vacunacion_instance, many= False)

        nodulo_instance = Nodulos.objects.create(ecop=ecop_instance, **nodulos_data)
        nodulos_json = NodulosSerializer(nodulo_instance, many= False)

        mucosa_instance = Mucosa.objects.create(ecop = ecop_instance, **mucosas_data)
        mucosa_json = MucosaSerializer(mucosa_instance, many= False)

        json_data = []
        json_data.append(ecop_json.data)
        json_data.append(sistema_json.data)
        json_data.append(problema_json.data)
        json_data.append(diagnostico_json.data)
        json_data.append(terapia_json.data)
        json_data.append(autorizado_json.data)
        json_data.append(mucosa_json.data)
        json_data.append(desparacitacion_json.data)
        json_data.append(vacunacion_json.data)
        json_data.append(nodulos_json.data)

        return Response({'Message': 'La intancia de Ecop para esta mascota se ha creado exitosamente!',
                             'data': json_data},
                            status=HTTP_201_CREATED)