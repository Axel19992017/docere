from django.contrib import admin
from .models import *

# Register your models here.
class SectionAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(SectionAdmin, self).__init__(model, admin_site)

admin.site.register(Section, SectionAdmin)

class TopicAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(TopicAdmin, self).__init__(model, admin_site)

admin.site.register(Topic, TopicAdmin)

class DocumentAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(DocumentAdmin, self).__init__(model, admin_site)

admin.site.register(Document, DocumentAdmin)