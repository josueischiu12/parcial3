from rest_framework import serializers
from .models import Grado, Estudiante

class GradoSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Grado
        fields = '__all__'

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'