from django.contrib import admin
from .models import Enrollment, VirtualRoom
# Register your models here.

admin.site.register(VirtualRoom)
admin.site.register(Enrollment)
