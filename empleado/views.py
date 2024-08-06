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
    def validar_login(self, request):
        nro_documento = request.query_params.get('nro_documento')
        contraseña = request.query_params.get('contrasena') 
        
        if not nro_documento or not contraseña:
            return Response({'error': 'Número de documento y contraseña son requeridos'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            empleado = Empleado.objects.get(nro_documento=nro_documento)
            if contraseña == empleado.contrasena:  # Comparar contraseñas en texto claro
                return Response({'mensaje': 'Login exitoso'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Contraseña incorrecta'}, status=status.HTTP_401_UNAUTHORIZED)
        except Empleado.DoesNotExist:
            return Response({'error': 'Empleado no encontrado'}, status=status.HTTP_404_NOT_FOUND)

class TipoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer
