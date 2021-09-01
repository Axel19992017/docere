from django.urls import path, include
from . import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('', include('apps.virtualroom.api.routers')),
]
