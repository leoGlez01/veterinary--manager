
# Imports
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import *
from Ecop.domain.models import *
from Ecop.application.Serializers.all_serializers import *
from Ecop.application.Serializers.historia_serializer import *

'''Use Case for Get Clinical Histories for Pet'''
@api_view(['GET'])
def obtener_historias(request, pk):
    historias_json = []
    mascotas_json = []
    tutores_json = []
    terapias_json = []
    vacunaciones_json = []
    desparacitaciones_json = []
    historias_json = []
    diagnosticos_json = []
    mucosas_json = []
    nodulos_json = []
    problemas_json = []
    sistemas_json = []
    autorizados_json = []

    mascota_instance = Mascota.objects.get(id=pk)
    mascota_json = MascotaSerializer(mascota_instance, many= False).data
    mascotas_json.append(mascota_json)

    tutor_instance = Tutor.objects.get(id= mascota_json.get('tutor'))
    tutor_json = TutorSerializer(tutor_instance, many=False).data
    tutores_json.append(tutor_json)

    if not mascota_instance:
        return Response({'Message': 'La mascota aun no tiene historia clinica'},
                        status=HTTP_404_NOT_FOUND)
    else:
        ecops = Ecop.objects.filter(mascota=pk)
        if not ecops:
            return Response({'mascota': mascotas_json, 'tutor': tutores_json}, status=HTTP_200_OK)
        else:
            for ecop in ecops:
                vacunas = Vacunacion.objects.filter(ecop= ecop)
                desparacitaciones = Desparacitacion.objects.filter(ecop= ecop)
                terapias = Terapia.objects.filter(ecop= ecop)
                diagnosticos = Diagnostico.objects.filter(ecop= ecop)
                mucosas = Mucosa.objects.filter(ecop= ecop)
                nodulos = Nodulos.objects.filter(ecop= ecop)
                problemas = Problema.objects.filter(ecop= ecop)
                sistemas = Sistema.objects.filter(ecop= ecop)
                autorizado = Autorizado.objects.filter(ecop= ecop)

                historia_json = EcopSerializer(ecop, many= False).data
                diagnostico_json = DiagnosticoSerializer(diagnosticos, many= True).data
                mucosa_json = MucosaSerializer(mucosas, many= True).data
                nodulo_json = NodulosSerializer(nodulos, many= True).data
                problema_json = ProblemaSerializer(problemas, many = True).data
                sistema_json = SistemaSerializer(sistemas, many = True).data
                vacunas_json = VacunacionSerializer(vacunas, many= True).data
                desparacitacion_json = DesparacitacionSerializer(desparacitaciones, many= True).data
                terapia_json = TerapiaSerializer(terapias, many= True).data
                autorizado_json = AutorizadoSerializer(autorizado, many= True).data
                
                terapias_json.append(terapia_json)
                vacunaciones_json.append(vacunas_json)
                desparacitaciones_json.append(desparacitacion_json)
                historias_json.append(historia_json)
                diagnosticos_json.append(diagnostico_json)
                mucosas_json.append(mucosa_json)
                nodulos_json.append(nodulo_json)
                problemas_json.append(problema_json)
                sistemas_json.append(sistema_json)
                autorizados_json.append(autorizado_json)

            return Response({'mascota':mascotas_json,
                            'tutor':tutores_json,
                            'general':historias_json,
                            'diagnosticos':diagnosticos_json,
                            'vacunaciones':vacunaciones_json,
                            'desparacitaciones':desparacitaciones_json,
                            'mucosas':mucosas_json,
                            'nodulos':nodulos_json,
                            'problemas':problemas_json,
                            'sistemas':sistemas_json,
                            'plan_terapeutico':terapias_json,
                            'pasantes':autorizados_json},
                            status=HTTP_200_OK)
