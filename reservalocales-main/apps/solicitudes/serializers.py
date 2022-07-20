from rest_framework import serializers
from apps.solicitudes.models import Solicitud
from typing import *


class SolicitudesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'