from django.db import models

# Create your models here.
class Grado(models.Model):
    """Model definition for Grado."""
    SEC = [
        ("A", "Seccion A"),
        ("B", "Seccion B"),
        ("C", "Seccion C"),
        ("D", "Seccion D"),
        ("E", "Seccion E"),
    ]

    SEM = [
        ("2S", "Segundo semestre"),
        ("4S", "Cuarto semestre"),
        ("6S", "Sexto semestre"),
        ("8S", "Octavo semestre"),
    ]

    CAR = [
        ("IS", "Ingenieria en Sistemas"),
        ("IE", "Ingenieria en Electronica"),
        ("IT", "Ingenieria en Telecomunicaciones"),
        ("IC", "Ingenieria Civil"),
    ]

    codigo = models.CharField(max_length=10)
    carrera = models.CharField(max_length=5, choices=CAR)
    semestre = models.CharField(max_length=5, choices=SEM)
    seccion = models.CharField(max_length=5, choices=SEC)


    # TODO: Define fields here

    class Meta:
        """Meta definition for Grado."""

        verbose_name = 'Grado'
        verbose_name_plural = 'Grados'

    def __str__(self):
        """Unicode representation of Grado."""
        return self.codigo

class Estudiante(models.Model):
    ACT = [
        ("Ng", "Ninguna"),
        ("Vj", "Videojuegos"),
        ("Rg", "Robogallitos"),
        ("Pp", "Presentacion de Proyectos"),
        ("Ex", "Exposicion"),
        ("St", "Staff"),
    ]

    """Model definition for Estudiante."""
    carnet = models.IntegerField()
    nombre1 = models.CharField(max_length=20, blank=True)
    nombre2 = models.CharField(max_length=20, blank=True)
    nombre3 = models.CharField(max_length=50, blank=True)
    apellido1 = models.CharField(max_length=20, blank=True)
    apellido2 = models.CharField(max_length=20, blank=True)
    grado = models.ForeignKey(Grado, on_delete=models.PROTECT)
    actividad = models.CharField(max_length=4, choices=ACT)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Estudiante."""

        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        """Unicode representation of Estudiante."""
        return str(self.carnet) + ' ' + self.nombre1 + ' ' + self.apellido1
