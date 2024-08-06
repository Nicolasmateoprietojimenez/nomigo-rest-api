from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Empleado, Rol, TipoDocumento
from .serializers import EmpleadoSerializer, RolSerializer, TipoDocumentoSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    
    @action(detail=False, methods=['get'])
    def saludar(self, request):
        nro_documento = request.query_params.get('nro_documento')
        if not nro_documento:
            return Response({'error': 'Número de documento no proporcionado'}, status=400)
            
        try:
            empleado = Empleado.objects.get(nro_documento=nro_documento)
            saludo = f"Hola, {empleado.nombres} {empleado.apellidos}!"
            return Response({'saludo': saludo})
        except Empleado.DoesNotExist:
            return Response({'error': 'Empleado no encontrado'}, status=404)

class TipoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer
