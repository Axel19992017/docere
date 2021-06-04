from django.urls import path

from . import views
from django.conf.urls import url


urlpatterns = [
    path("accounts/profile/", views.profile, name="myprofile"),
]