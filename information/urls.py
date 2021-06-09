
from django.urls import path, include
from .views import *

urlpatterns = [
    path('create-section', create_section, name="createseccion"),
]