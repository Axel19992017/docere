from django.urls import path

from . import views
from django.conf.urls import url


urlpatterns = [
    path("register/", views.register, name="register"),
]

urlpatterns += [
    url('personalinformation/create/$', views.PersonalInformationCreate.as_view(), name='personalinformation_create'),
    url('personalinformation/(?P<pk>\d+)/update/$', views.PersonalInformationUpdate.as_view(), name='personalinformation_update'),
    url('user/(?P<pk>\d+)/update/$', views.UserUpdate.as_view(), name='user_update'),
    url('profile/(?P<pk>\d+)/', views.profile_id, name='profile'),
]