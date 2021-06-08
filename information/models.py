from django.db import models
from virtualroom.models import *
from docere.models import TimeStamped
# Create your models here.

class Section(TimeStamped):
    name = models.CharField(max_length=50, verbose_name="Nombre")




class Topic(TimeStamped):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.CharField(max_length=300, verbose_name="Descripción", blank=True)
    section = models.ForeignKey(Section, verbose_name="Sección", related_name="topics", on_delete=models.CASCADE)
    virtualroom = models.ForeignKey(VirtualRoom, verbose_name="Clase virtual", on_delete=models.CASCADE, related_name="topics")

class Document(TimeStamped):
    file = models.FileField(upload_to="topics/%Y/%m/%d")
    topic = models.ForeignKey(Topic, verbose_name="archivos", on_delete=models.CASCADE)

    