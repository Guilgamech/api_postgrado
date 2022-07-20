from rest_framework.routers import DefaultRouter
from apps.users.views import UserView, LogoutView
from apps.local.views import LocalView
from apps.solicitudes.views import SolicitudesView
from apps.aseguramiento.views import AseguramientoView
from apps.actividad.views import ActividadView


router = DefaultRouter()
router.register(prefix='users', basename='users', viewset=UserView)
router.register(prefix='logout-token', basename='logout', viewset=LogoutView)
router.register(prefix='local', basename='locales',
                viewset=LocalView)
router.register(prefix='solicitud', basename='solicitudes',
                viewset=SolicitudesView)
router.register(prefix='aseguramiento',
                basename='aseguramientos', viewset=AseguramientoView)
router.register(prefix='actividad',
                basename='actividades', viewset=ActividadView)

