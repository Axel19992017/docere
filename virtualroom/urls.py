from django.urls import path, include
from .views import *
from virtualroom import views
from django.conf.urls import url

urlpatterns = [
    path('', index, name="virtualrooms"),
    path('archived', index_archived, name="virtualroomsarchived"),
    path('enrolled', index_enrolled, name="virtualroomsenrolled" ),
    path('search', virtual_room_search, name="virtualroomsearch"),
    path('notifications', virtual_room_notifications, name="virtualroomsnotifications"),
    path('<int:pk>/details', virtual_room_detail, name="virtualroomdetail"),
    path('<int:pk>/search', virtual_room_enroll, name="virtualroomenroll"),
    path('<int:pk>/<str:option>/<int:pk_user>', set_status_enrolled, name="setstatusenrolled"),
]

urlpatterns += [
    url('create/$', views.VirtualRoomCreate.as_view(), name='virtualroom_create'),
    url('(?P<pk>\d+)/update/$', views.VirtualRoomUpdate.as_view(), name='virtualroom_update'),
    url('(?P<pk>\d+)/delete/$', views.VirtualRoomDelete.as_view(), name='virtualroom_delete'),
    url('(?P<pk>\d+)/archive/$', views.virtual_room_archive, name='virtualroom_archive'),
]