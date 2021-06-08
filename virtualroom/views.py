from django.shortcuts import redirect, render
from .models import VirtualRoom, VirtualRoomStatus, EnrollmentStatus
from django.contrib.auth.decorators import login_required
from django.db.models import Q
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
        "options": True,
        "title": "Mis clases",
    }
    return render(request, "virtualroom/dashboard.html", context)

@login_required
def index_archived(request):

    classes = VirtualRoom.objects.filter(creator=request.user, status=VirtualRoomStatus.DEACTIVATE)
    context = {
        "rooms": classes,
        "options": True,
        "title": "Mis clases archivadas",
    }
    return render(request, "virtualroom/dashboard.html", context)

@login_required
def index_enrolled(request):

    enrolleds = request.user.enrollments.filter(state=EnrollmentStatus.ACCEPTED)
    classes = []
    for enroll in enrolleds:
        classes.append(enroll.virtualroom)


    context = {
        "rooms": classes,
        "options": False,
        "title": "Clases en las que me matriculé ",
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

@login_required
def virtual_room_search(request):
    if request.method == "POST":
        search = request.POST.get("search")
    
        classes = VirtualRoom.objects.filter((Q(name__icontains=search) | Q(description__icontains=search)) & Q(is_private=False)).all()
        context = {
            "rooms": classes,
            "options": False,
            "title": "Resultados ",
        }
        return render(request, "virtualroom/dashboard.html", context)
    else:
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