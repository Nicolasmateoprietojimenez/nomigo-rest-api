from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RolViewSet, EmpleadoViewSet, TipoDocumentoViewSet

router = DefaultRouter()
router.register(r'roles', RolViewSet)
router.register(r'empleado', EmpleadoViewSet)
router.register(r'tipodocumento', TipoDocumentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
