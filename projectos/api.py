#creamos nuestras viewset para la api
from .models import Projecto
from rest_framework import viewsets, permissions
from .serializers import ProjectoSerializacion

#creamos nuestra primera viewset
class ProjectoViewSet(viewsets.ModelViewSet):
    
    queryset = Projecto.objects.all()
    #le indicamos quien puede usar esta viewset
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectoSerializacion