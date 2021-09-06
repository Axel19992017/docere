from .serializers import VirtualRoomSerializer, EnrollmentSerializer
from apps.virtualroom.models import VirtualRoom, Enrollment
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class VirtualRoomViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = VirtualRoomSerializer
    queryset = VirtualRoom.objects.all()


class EnrollmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = VirtualRoomSerializer
    queryset = Enrollment.objects.all()