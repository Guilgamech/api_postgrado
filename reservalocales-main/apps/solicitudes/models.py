from django.db import models
from django.db.models import Q
from rest_framework.exceptions import ValidationError

from apps.actividad.models import TipoActividad, Actividad
from apps.local.models import Local
from apps.users.models import Trabajador


class Estado(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(max_length=255, null=True, blank=True)
    observacion = models.TextField(max_length=255, null=True, blank=True)
    fechaInicio = models.DateField('fecha de inicio')
    fechaFin = models.DateField('fecha de fin')
    horaInicio = models.TimeField('hora de inicio', null=True, blank=True)
    horaFin = models.TimeField('hora de fin', null=True, blank=True)
    diaCompleto = models.BooleanField('todo el día', default=False)
    cantidadParticipante = models.IntegerField(null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=1)
    solicitante = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    tipoActividad = models.ForeignKey(TipoActividad, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'


    def clean(self):
        try:
            # Validar que la fecha de inicio sea anterior a la fecha de fin
            if self.fechaInicio > self.fechaFin:
                raise ValidationError({
                    'fechaInicio': ValidationError('La fecha de inicio debe ser anterior a la fecha de fin',
                                                   code='too_late_date'),
                    'fechaFin': ValidationError('La fecha de fin debe ser posterior a la fecha de inicio',
                                                code='too_early_date'),
                })

            actividad = Actividad.objects.filter(local=self.local).filter(
                Q(fechaInicio__gte=self.fechaInicio, fechaFin__gte=self.fechaFin) &
                (Q(horaInicio__gte=self.horaInicio, horaFin__gt=self.horaInicio) |
                Q(horaInicio__lte=self.horaInicio, horaFin__gt=self.horaInicio))
            ).exclude(id=self.pk)

            if actividad.count() != 0:
                message = "El lugar con el rango de fecha y hora coincide con alguna otra actividad planificada"
                raise ValidationError({
                    '__all__': message,
                    'local': "El lugar: " + self.local.__str__() + " está ocupado en ese momento.",
                    'fechaInicio': "Fecha ocupada",
                    'fechaFin': "Fecha ocupada",
                    'horaInicio': "Hora ocupada",
                    'horaFin': "Hora ocupada",
                })
            hayDatos = Solicitud.objects.all()
            if hayDatos.count() != 0:
                # Buscar solicitudes en el mismo lugar y rango de fecha de un solicitante
                solicitud = Solicitud.objects.filter(solicitante=self.solicitante).filter(local=self.local).filter(
                    Q(fechaInicio__gte=self.fechaInicio, fechaFin__gte=self.fechaFin) &
                    (Q(horaInicio__gte=self.horaInicio, horaFin__gt=self.horaInicio) |
                    Q(horaInicio__lte=self.horaInicio, horaFin__gt=self.horaInicio))
                ).exclude(id=self.pk)
                # Validar que no haya solicitudes en el mismo lugar y rango de fecha
                if solicitud.count() != 0:
                    message = "El lugar con el rango de fecha y hora coincide con alguna otra solicitud"
                    raise ValidationError({
                        '__all__': message,
                        'local': "El lugar: " + self.local.__str__() + " está ocupado en ese momento.",
                        'fechaInicio': "Fecha ocupada",
                        'fechaFin': "Fecha ocupada",
                        'horaInicio': "Hora ocupada",
                        'horaFin': "Hora ocupada",
                    })
        except (Local.DoesNotExist):
            pass


    def __str__(self):
        return self.nombre