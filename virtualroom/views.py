from django.shortcuts import redirect, render
from .models import VirtualRoom, VirtualRoomStatus, EnrollmentStatus
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
@login_required
def index(request):

    classes = VirtualRoom.objects.filter(creator=request.user, status=VirtualRoomStatus.ACTIVE)
    context = {
        "rooms": classes,
        "archived": False,
    }
    return render(request, "virtualroom/dashboard.html", context)

@login_required
def index_archived(request):

    classes = VirtualRoom.objects.filter(creator=request.user, status=VirtualRoomStatus.DEACTIVATE)
    context = {
        "rooms": classes,
        "archived": True,
    }
    return render(request, "virtualroom/dashboard.html", context)

@login_required
def virtual_room_archive(request, pk):
    vr = VirtualRoom.objects.get(pk=pk)
    if(vr.status == VirtualRoomStatus.ACTIVE):
        vr.status = VirtualRoomStatus.DEACTIVATE
        vr.save()
        messages.error(request, 'La clase está archivada.')
    else:
        vr.status = VirtualRoomStatus.ACTIVE
        vr.save()
        messages.info(request, 'La clase está desarchivada.')
    return redirect('virtualrooms')


class VirtualRoomCreate(LoginRequiredMixin, CreateView):
    model = VirtualRoom
    fields= ['name', 'description', 'is_private', 'photo']
    success_url = reverse_lazy('virtualrooms')
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.creator = self.request.user
        return super().form_valid(form)


class VirtualRoomUpdate(LoginRequiredMixin, UpdateView):
    model = VirtualRoom
    fields= ['name', 'description', 'is_private', 'photo']
    success_url = reverse_lazy('virtualrooms')

class VirtualRoomDelete(LoginRequiredMixin, DeleteView):
    model = VirtualRoom
    template_name="delete_object.html"
    success_url = reverse_lazy('virtualrooms')