from rest_framework import serializers
from apps.local.models import Local
from typing import *


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = '__all__'