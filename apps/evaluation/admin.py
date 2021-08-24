from django.contrib import admin
from .models import *

# Register your models here.

class EvaluationAdmin(admin.ModelAdmin):
    list_filter =['virtualroom']
    search_fields = ['name', 'description']
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(EvaluationAdmin, self).__init__(model, admin_site)

admin.site.register(Evaluation, EvaluationAdmin)
class PuntuationAdmin(admin.ModelAdmin):
    list_filter =['evaluation', 'enrollment', 'evaluation__virtualroom']

    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(PuntuationAdmin, self).__init__(model, admin_site)

admin.site.register(Puntuation, PuntuationAdmin)