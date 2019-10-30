from rest_framework import viewsets 
from .models import Grado, Estudiante 
from .serializers import GradoSerializer, EstudianteSerializer 

class GradoViewSet (viewsets.ModelViewSet): 
    queryset = Grado.objects.all() 
    serializer_class = GradoSerializer

class EstudianteViewSet (viewsets.ModelViewSet): 
    queryset = Estudiante.objects.all() 
    serializer_class = EstudianteSerializer
