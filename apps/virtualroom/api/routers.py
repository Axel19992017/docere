from rest_framework import routers
from .views import VirtualRoomViewSet, EnrollmentViewSet

router = routers.SimpleRouter()

router.register(r'virtualrooms', VirtualRoomViewSet)
router.register(r'enrollments', EnrollmentViewSet)

urlpatterns = router.urls