from rest_framework import serializers
from Ecop.domain.models import Mascota, Diagnostico, Vacunacion, Desparacitacion


class CustomPetSerializer(serializers.ModelSerializer):
    fecha_consulta = serializers.SerializerMethodField()

    class Meta:
        model = Mascota
        fields = '__all__'

    def get_fecha_consulta(self, obj):
        return obj.fecha_consulta.strftime("%Y-%m-%d")