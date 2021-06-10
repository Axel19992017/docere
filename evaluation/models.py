from django.db import models
from docere.models import TimeStamped
from virtualroom.models import Enrollment, VirtualRoom
from django.conf import settings
# Create your models here.



class Evaluation(TimeStamped):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.CharField(max_length=200, verbose_name="Descripción", blank=True)
    virtualroom = models.ForeignKey(VirtualRoom, related_name="evaluations",verbose_name="Clase", on_delete=models.CASCADE)
    enrollments = models.ManyToManyField(Enrollment, through="Puntuation", verbose_name="Estudiantes", related_name="evaluations")


class Puntuation(TimeStamped):
    evaluation = models.ForeignKey(Evaluation, verbose_name="Evaluación",related_name="puntuations", on_delete=models.CASCADE)
    enrollment =  models.ForeignKey(Enrollment, verbose_name="Inscripción del estudiante",related_name="puntuations", on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name="Cantidad")
    observation = models.CharField(max_length=150, verbose_name="Observaciones", blank=True)

    def __str__(self):
        return f"{self.amount}, por {self.enrollment}"


