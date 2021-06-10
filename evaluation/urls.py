
from django.urls import path, include
from .views import *

urlpatterns = [
    path('create', create_evaluation, name="createevaluation"),
    path('<int:pk_e>/update', update_evaluation, name="updateevaluation"),
    path('<int:pk_e>/delete', delete_evaluation, name="deleteevaluation"),
    # recibirá en post los demás datos
    path('<int:pk_e>/puntuation', create_puntuation, name="createpuntuation"),
    path('<int:pk_e>/puntuation/update', update_puntuation, name="updatepuntuation"),
]