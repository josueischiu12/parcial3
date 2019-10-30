from rest_framework import routers
from citein.viewsets import GradoViewSet, EstudianteViewSet

router = routers.DefaultRouter()

router.register(r'grado', GradoViewSet)
router.register(r'estudiante', EstudianteViewSet)