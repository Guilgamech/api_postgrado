from django.db import models

from apps.local.models import Local
from apps.solicitudes.models import Solicitud


class TipoAseguramiento(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre

class Aseguramiento(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    tipoAseguramiento = models.ForeignKey(TipoAseguramiento, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Aseguramineto'
        verbose_name_plural = 'Aseguramientos'


    def __str__(self):
        return self.nombre

class AseguramientoLocal(models.Model):
    aseguramiento = models.ForeignKey(Aseguramiento, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.local.__str__() + ' - ' + self.aseguramiento.__str__()

class AseguramientoSolicitud(models.Model):
    aseguramiento = models.ForeignKey(Aseguramiento, on_delete=models.CASCADE)
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=255, null=True)
    observacion = models.TextField(max_length=255, null=True)

    def __str__(self):
        return self.solicitud.__str__() + ' - ' + self.aseguramiento.__str__()
