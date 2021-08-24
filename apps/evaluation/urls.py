
from django.urls import path, include
from .views import *

urlpatterns = [
    path('<int:pk_vr>/create', create_evaluation, name="createevaluation"),
    path('<int:pk_e>/update', update_evaluation, name="updateevaluation"),
    path('<int:pk_e>/delete', delete_evaluation, name="deleteevaluation"),
    # recibirá en post los demás datos
    path('<int:pk_e>/puntuation/<int:pk_s>/', create_puntuation, name="createpuntuation"),
    path('puntuation/<int:pk_p>/update', update_puntuation, name="updatepuntuation"),
    path('puntuation/<int:pk_p>/delete', delete_puntuation, name="deletepuntuation"),
]