from django.contrib import admin

# Register your models here.
from apps.actividad.models import Actividad
from apps.local.models import Local
from apps.solicitudes.models import Solicitud
from apps.users.models import Trabajador
from apps.aseguramiento.models import Aseguramiento


admin.site.register(Actividad)
admin.site.register(Local)
admin.site.register(Solicitud)
admin.site.register(Trabajador)
admin.site.register(Aseguramiento)
