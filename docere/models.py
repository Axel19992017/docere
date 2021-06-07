from django.utils import timezone
from django.db import models

# https://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add/1737078#1737078
class TimeStamped(models.Model):
    creation_date = models.DateTimeField(editable=False)
    last_modified = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = timezone.now()

        self.last_modified = timezone.now()
        return super(TimeStamped, self).save(*args, **kwargs)

    class Meta:
        abstract = True