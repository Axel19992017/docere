from django import forms
from django.forms import ClearableFileInput
from .models import Document, Topic


class TopicModelForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name', 'description']

class DocumentModelForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file']
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True}),
        }
