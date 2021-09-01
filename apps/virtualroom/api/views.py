from .serializers import VirtualRoomSerializer, EnrollmentSerializer
from apps.virtualroom.models import VirtualRoom, Enrollment
from rest_framework import viewsets


class VirtualRoomViewSet(viewsets.ModelViewSet):

    serializer_class = VirtualRoomSerializer
    queryset = VirtualRoom.objects.all()


class EnrollmentViewSet(viewsets.ModelViewSet):

    serializer_class = VirtualRoomSerializer
    queryset = Enrollment.objects.all()