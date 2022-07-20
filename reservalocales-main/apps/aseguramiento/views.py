from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.aseguramiento.serializers import *


class AseguramientoView(viewsets.ModelViewSet):
    serializer_class = AseguramientoSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Aseguramiento.objects.all()
