
from django.urls import path, include
from .views import *

urlpatterns = [
    path('create-section', create_section, name="createseccion"),
    path('<int:pk_s>/create-topic', create_to_topic, name="createtopic"),
    path('<int:pk_t>/edit-topic', edit_topic, name="edittopic"),
    path('<int:pk_t>/delete-topic', delete_topic, name="deletetopic"),


]