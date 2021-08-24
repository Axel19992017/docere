from django.db import models
from docere.models import TimeStamped
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

# Create your models here.
class PersonalInformation(TimeStamped):
    user= models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="Usuario", related_name="information",on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/', verbose_name="Foto", blank=True)
    web_page = models.CharField(max_length=50, verbose_name="Página web", blank=True)
    ocupation = models.CharField(max_length=50, verbose_name="Ocupación Actual", blank=True)
    phone = models.CharField(max_length=15, verbose_name="Teléfono Móvil", blank=True)
    facebook_link = models.CharField(max_length=50,verbose_name="Facebook", blank=True)
    twitter_link = models.CharField(max_length=50,verbose_name="Twitter", blank=True)
    instagram_link = models.CharField(max_length=50,verbose_name="Instagram", blank=True)
    linkedin_link = models.CharField(max_length=100,verbose_name="Linkedin", blank=True)

    class Meta:
        verbose_name = "Información del usuario"
        verbose_name_plural = "Información de los usuarios"

@receiver(post_delete, sender=PersonalInformation)
def photo_delete(sender, instance, **kwargs):
    instance.photo.delete(False)

# https://www.it-swarm-es.com/es/python/como-eliminar-una-imagen-antigua-al-actualizar-imagefield/969564306/
@receiver(pre_save, sender=PersonalInformation)
def delete_file_on_change_extension(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_photo = PersonalInformation.objects.get(pk=instance.pk).photo
        except PersonalInformation.DoesNotExist:
            return
        else:
            new_photo = instance.photo
            if old_photo and old_photo.url != new_photo.url:
                old_photo.delete(save=False)