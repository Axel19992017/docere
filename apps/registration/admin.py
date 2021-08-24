from django.contrib import admin
from .models import PersonalInformation
from django.contrib.auth.models import User
from django.db.models import ManyToOneRel, ForeignKey, OneToOneField


# Register your models here.

class PersonalInformationAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(PersonalInformationAdmin, self).__init__(model, admin_site)

admin.site.register(PersonalInformation, PersonalInformationAdmin)
