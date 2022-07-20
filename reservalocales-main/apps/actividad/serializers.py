from rest_framework import serializers
from apps.actividad.models import Actividad
from typing import *


class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = '__all__'