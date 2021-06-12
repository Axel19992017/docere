from django.contrib import admin
from .models import Enrollment, VirtualRoom
# Register your models here.

class VirtualRoomAdmin(admin.ModelAdmin):
    list_filter =['creator', 'is_private', 'status']
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(VirtualRoomAdmin, self).__init__(model, admin_site)

admin.site.register(VirtualRoom, VirtualRoomAdmin)
class EnrollmentAdmin(admin.ModelAdmin):

    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(EnrollmentAdmin, self).__init__(model, admin_site)

admin.site.register(Enrollment, EnrollmentAdmin)
