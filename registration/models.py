from django.db import models
from docere.models import TimeStamped
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
class PersonalInformation(TimeStamped):
    user= models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="Usuario", related_name="information",on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/', verbose_name="Foto", blank=True)
    web_page = models.CharField(max_length=50, verbose_name="Página web", blank=True)
    facebook_link = models.CharField(max_length=50,verbose_name="Facebook", blank=True)
    twitter_link = models.CharField(max_length=50,verbose_name="Twitter", blank=True)
    instagram_link = models.CharField(max_length=50,verbose_name="Instagram", blank=True)
    linkedin_link = models.CharField(max_length=100,verbose_name="Linkedin", blank=True)

@receiver(post_delete, sender=PersonalInformation)
def photo_delete(sender, instance, **kwargs):
    instance.photo.delete(False)