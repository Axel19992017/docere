from django.contrib import admin
from .models import *

# Register your models here.
class SectionAdmin(admin.ModelAdmin):
    list_filter =['virtualroom']
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(SectionAdmin, self).__init__(model, admin_site)

admin.site.register(Section, SectionAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_filter =['section__virtualroom', 'section']
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(TopicAdmin, self).__init__(model, admin_site)

admin.site.register(Topic, TopicAdmin)

