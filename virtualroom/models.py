from django.db import models
from docere.models import TimeStamped
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver



class VirtualRoomStatus(models.IntegerChoices):
    ACTIVE = 0, 'Clase Virtual Activada'
    DEACTIVATE = 1, 'Clase Virtual Archivada'

# https://openwebinars.net/blog/tutorial-django-modelos-bbdd-donde-guardar-informacion/
class VirtualRoom(TimeStamped):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Creador de la Clase Virtual", on_delete=models.CASCADE, related_name="virtualroomscreated")
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Enrollment', verbose_name="Estudiantes", related_name="virtualrooms")
    description = models.CharField(max_length=50, verbose_name="Descripción")
    is_private = models.BooleanField(verbose_name="Es privado")
    photo = models.ImageField(upload_to='virtualrooms/', verbose_name="Foto", blank=True)
    status = models.IntegerField(default=VirtualRoomStatus.ACTIVE,choices=VirtualRoomStatus.choices)



@receiver(post_delete, sender=VirtualRoom)
def photo_delete(sender, instance, **kwargs):
    instance.photo.delete(False)


class EnrollmentStatus(models.IntegerChoices):
    DISMISSED = 0, 'No aceptado'
    USER_PENDING = 1, 'Pendiente que acepte el estudiante'
    TEACHER_PENDING = 2, 'Pendiente que acepte el profesor'
    ACCEPTED = 3, 'Aceptado'
    EXPELLED = 4, 'Expulsado'
    RETIRED = 5, 'Abandonó la clase virtual'

class EnrollmentRols(models.IntegerChoices):
    STUDENT = 0, 'Estudiante'
    TEACHER = 1, 'Profesor'


class Enrollment(TimeStamped):
    virtualroom = models.ForeignKey(VirtualRoom, verbose_name="Clase virtual", on_delete=models.CASCADE, related_name="enrollments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Usuario", on_delete=models.CASCADE, related_name="enrollments")
    state = models.IntegerField(choices=EnrollmentStatus.choices)
    rol = models.IntegerField(choices=EnrollmentRols.choices)
    