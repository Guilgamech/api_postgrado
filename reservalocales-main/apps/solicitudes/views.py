from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.solicitudes.serializers import *

# Create your views here.

class SolicitudesView(viewsets.ModelViewSet):
    serializer_class = SolicitudesSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Solicitud.objects.all()
