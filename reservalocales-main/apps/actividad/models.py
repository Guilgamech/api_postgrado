from django.db import models
from django.db.models import Q
from rest_framework.exceptions import ValidationError

from apps.local.models import Local


class TipoActividad(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre



class Actividad(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(max_length=255, null=True, blank=True)
    fechaInicio = models.DateField('fecha de inicio', null=False, blank=False)
    fechaFin = models.DateField('fecha de fin', null=False, blank=False)
    horaInicio = models.TimeField('hora de inicio', null=False, blank=False)
    horaFin = models.TimeField('hora de fin', null=False, blank=False)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    tipoActividad = models.ForeignKey(TipoActividad, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'

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

            actividad = Actividad.objects.filter( local=self.local).filter(
                Q(fechaInicio__gte=self.fechaInicio, fechaFin__gte=self.fechaFin) &
                (Q(horaInicio__gte=self.horaInicio, horaFin__gt=self.horaInicio) |
                Q(horaInicio__lte=self.horaInicio, horaFin__gt=self.horaInicio))
            ).exclude(id=self.pk)

            if actividad.count() > 0:
                message = "El lugar y rango de fecha coincide con los de otra actividad"
                if self.local:
                    raise ValidationError({
                        '__all__': message,
                        'local': "El lugar: " + self.local.__str__() + " está ocupado",
                        'fechaInicio': "Fecha ocupada",
                        'fechaFin': "Fecha ocupada",
                        'horaInicio': "Hora ocupada",
                        'horaFin': "Hora ocupada",
                    })
        except (Local.DoesNotExist):
            pass

    def __str__(self):
        return self.nombre

