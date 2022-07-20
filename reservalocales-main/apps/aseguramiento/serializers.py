from rest_framework import serializers
from apps.aseguramiento.models import Aseguramiento
from typing import *


class AseguramientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aseguramiento
        fields = '__all__'