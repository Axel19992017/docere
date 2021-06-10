from django.db import models
from virtualroom.models import *
from docere.models import TimeStamped
# Create your models here.
# https://stackoverflow.com/questions/38257231/how-can-i-upload-multiple-files-to-a-model-field/52016594
class Section(TimeStamped):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    virtualroom = models.ForeignKey(VirtualRoom, verbose_name="Clase virtual", on_delete=models.CASCADE, related_name="sections", blank=True)

class Topic(TimeStamped):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.CharField(max_length=300, verbose_name="Descripción", blank=True)
    section = models.ForeignKey(Section, verbose_name="Sección", related_name="topics", on_delete=models.CASCADE)
class Document(TimeStamped):
    file = models.FileField(upload_to="topics/%Y/%m/%d")
    topic = models.ForeignKey(Topic, verbose_name="archivos", on_delete=models.CASCADE, related_name="documents")

    