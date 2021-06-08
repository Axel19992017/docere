from django.urls import path, include
from .views import index, index_archived, index_enrolled, virtual_room_search, virtual_room_detail, set_status_enrolled
from virtualroom import views
from django.conf.urls import url

urlpatterns = [
    path('', index, name="virtualrooms"),
    path('archived', index_archived, name="virtualroomsarchived"),
    path('enrolled', index_enrolled, name="virtualroomsenrolled" ),
    path('search', virtual_room_search, name="virtualroomsearch"),
    path('<int:pk>/details', virtual_room_detail, name="virtualroomdetail"),
    path('<int:pk>/<str:option>', set_status_enrolled, name="setstatusenrolled"),
]

urlpatterns += [
    url('create/$', views.VirtualRoomCreate.as_view(), name='virtualroom_create'),
    url('(?P<pk>\d+)/update/$', views.VirtualRoomUpdate.as_view(), name='virtualroom_update'),
    url('(?P<pk>\d+)/delete/$', views.VirtualRoomDelete.as_view(), name='virtualroom_delete'),
    url('(?P<pk>\d+)/archive/$', views.virtual_room_archive, name='virtualroom_archive'),
]