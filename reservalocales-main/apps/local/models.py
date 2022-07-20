from django.db import models

# Create your models here.
from apps.users.models import Trabajador


class Local(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    ubicacion = models.CharField(max_length=255)
    capacidad = models.IntegerField()
    telefono = models.IntegerField(null=True, blank=True)
    responsables = models.ManyToManyField(Trabajador, blank=True, related_name='responsables')

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locales'


    def __str__(self):
        return self.nombre