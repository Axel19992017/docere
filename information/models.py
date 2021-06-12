from django.db import models
from virtualroom.models import *
from docere.models import TimeStamped
from django.db.models.signals import post_delete, pre_save
# Create your models here.
# https://stackoverflow.com/questions/38257231/how-can-i-upload-multiple-files-to-a-model-field/52016594
class Section(TimeStamped):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    virtualroom = models.ForeignKey(VirtualRoom, verbose_name="Clase virtual", on_delete=models.CASCADE, related_name="sections", blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Sección"
        verbose_name_plural ="Secciones"

class Topic(TimeStamped):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.CharField(max_length=300, verbose_name="Descripción", blank=True)
    section = models.ForeignKey(Section, verbose_name="Sección", related_name="topics", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Tema"
        verbose_name_plural ="Temas"
class Document(TimeStamped):
    file = models.FileField(upload_to="topics/%Y/%m/%d")
    topic = models.ForeignKey(Topic, verbose_name="archivos", on_delete=models.CASCADE, related_name="documents")

    def __str__(self):
        return self.file.name
    
    class Meta:
        verbose_name="Documento"
        verbose_name_plural ="Documentos"

@receiver(post_delete, sender=Document)
def file_delete(sender, instance, **kwargs):
    instance.file.delete(False)

# https://www.it-swarm-es.com/es/python/como-eliminar-una-imagen-antigua-al-actualizar-imagefield/969564306/
@receiver(pre_save, sender=Document)
def delete_file_on_change_extension(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_file = Document.objects.get(pk=instance.pk).file
        except Document.DoesNotExist:
            return
        else:
            new_file = instance.file
            if old_file and old_file.url != new_file.url:
                old_file.delete(save=False)