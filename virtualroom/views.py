from django.shortcuts import render
from .models import VirtualRoom, VirtualRoomStatus
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):

    classes = VirtualRoom.objects.filter(creator=request.user, status=VirtualRoomStatus.ACTIVE)
    context = {
        "rooms": classes
    }
    return render(request, "virtualroom/dashboard.html", context)