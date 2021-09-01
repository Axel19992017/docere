from apps.virtualroom.models import VirtualRoom, Enrollment
from rest_framework import serializers
class VirtualRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualRoom
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'