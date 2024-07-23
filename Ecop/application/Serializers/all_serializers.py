# Imports
from rest_framework.serializers import ModelSerializer
from Ecop.domain.models import *


"""Serializer for Tutor Model"""
class TutorSerializer(ModelSerializer):
    class Meta:
        model = Tutor
        fields = "__all__"


"""Serializer for Mascota Model"""
class MascotaSerializer(ModelSerializer):
    class Meta:
        model = Mascota
        fields = "__all__"


"""Serializer for Ecop Model"""
class EcopSerializer(ModelSerializer):
    class Meta:
        model = Ecop
        fields = "__all__"


"""Serializer for Autorizado Model"""
class AutorizadoSerializer(ModelSerializer):
    class Meta:
        model = Autorizado
        fields = "__all__"


"""Serializer for Desparacitacion Model"""
class DesparacitacionSerializer(ModelSerializer):
    class Meta:
        model = Desparacitacion
        fields = "__all__"


"""Serializer for Diagnostico Model"""
class DiagnosticoSerializer(ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = "__all__"


"""Serializer for Mucosa Model"""
class MucosaSerializer(ModelSerializer):
    class Meta:
        model = Mucosa
        fields = "__all__"


"""Serializer for Nodulos Model"""
class NodulosSerializer(ModelSerializer):
    class Meta:
        model = Nodulos
        fields = "__all__"


"""Serializer for Problema Model"""
class ProblemaSerializer(ModelSerializer):
    class Meta:
        model = Problema
        fields = "__all__"


"""Serializer for Sistema Model"""
class SistemaSerializer(ModelSerializer):
    class Meta:
        model = Sistema
        fields = "__all__"


"""Serializer for Terapia Model"""
class TerapiaSerializer(ModelSerializer):
    class Meta:
        model = Terapia
        fields = "__all__"


"""Serializer for Vacunacion Model"""
class VacunacionSerializer(ModelSerializer):
    class Meta:
        model = Vacunacion
        fields = "__all__"
