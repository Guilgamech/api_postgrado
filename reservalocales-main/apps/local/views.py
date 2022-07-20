from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.local.serializers import *

# Create your views here.

class LocalView(viewsets.ModelViewSet):
    serializer_class = LocalSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Local.objects.all()
