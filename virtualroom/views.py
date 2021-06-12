from django.shortcuts import redirect, render
from .models import VirtualRoom, VirtualRoomStatus, EnrollmentStatus, EnrollmentRols
from information.forms import DocumentModelForm, TopicModelForm
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
from virtualroom.models import Enrollment
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):

    classes = VirtualRoom.objects.filter(creator=request.user, status=VirtualRoomStatus.ACTIVE)
    context = {
        "rooms": classes,
        "options": True,
        "title": "Mis clases",
    }
    context["isactive"] = "virtualrooms"
    return render(request, "virtualroom/dashboard.html", context)

@login_required
def index_archived(request):

    classes = VirtualRoom.objects.filter(creator=request.user, status=VirtualRoomStatus.DEACTIVATE)
    context = {
        "rooms": classes,
        "options": True,
        "title": "Mis clases archivadas",
    }
    context["isactive"] = "virtualroomsarchived"
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
    context["isactive"] = "virtualroomsenrolled"
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
        # busca por username, first name, lastname, nombre y descripción de la asignatura
        classes = VirtualRoom.objects.filter((Q(name__icontains=search) | Q(description__icontains=search) | Q(creator__first_name__icontains=search) | Q(creator__last_name__icontains=search) | Q(creator__username__icontains=search)) & Q(is_private=False)).all()
        context = {
            "rooms": classes,
            "options": False,
            "title": "Resultados ",
        }
        return render(request, "virtualroom/dashboard.html", context)
    else:
        return redirect('virtualrooms')

@login_required
def virtual_room_notifications(request):
    pending_me = Enrollment.objects.filter(Q(virtualroom__creator = request.user) & Q(state = EnrollmentStatus.TEACHER_PENDING)).all()
    pending = Enrollment.objects.filter(Q(user = request.user) & Q(state = EnrollmentStatus.USER_PENDING)).all()
    context = {
        "pendings_me" : pending_me,
        "pendings" : pending,
    }
    context["isactive"] = "virtualroomsnotifications"
    return render(request, "virtualroom/notifications.html", context)

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


@login_required
def virtual_room_detail(request, pk):
    vr = VirtualRoom.objects.get(pk=pk)
    participants = vr.enrollments.filter(state=EnrollmentStatus.ACCEPTED).all()
    context = {
        "virtualroom": vr,
        "participants": participants
    }
    
    enrollment = Enrollment.objects.filter(user=request.user, virtualroom= vr).first()
    if request.user == vr.creator:
        context["enrollmentStatus"] = "Gestionar"
    elif not enrollment:
        context["enrollmentStatus"] = "No matriculado"
    elif enrollment.state == EnrollmentStatus.ACCEPTED:
        context["enrollmentStatus"] = "Ya eres miembro"
    elif enrollment.state == EnrollmentStatus.DISMISSED:
        context["enrollmentStatus"] = "Solicitud rechazada"
    elif enrollment.state == EnrollmentStatus.TEACHER_PENDING:
        context["enrollmentStatus"] = "Solicitud pendiente de que la acepten"
    elif enrollment.state == EnrollmentStatus.USER_PENDING:
        context["enrollmentStatus"] = "Solicitud pendiente de que la aceptes"
    elif enrollment.state == EnrollmentStatus.EXPELLED:
        context["enrollmentStatus"] = "Expulsado del grupo"
    elif enrollment.state == EnrollmentStatus.RETIRED:
        context["enrollmentStatus"] = "Abandonastes del grupo"
    else:
        context["enrollmentStatus"] = "Algo extraño pasó, revisa por favor."
    
    context["formAddTopic"] = TopicModelForm
    context["formAddTopicFields"] = DocumentModelForm
    context["enrollment"] = enrollment

    return render(request, "virtualroom/details.html", context)

@login_required 
def set_status_enrolled(request, pk, option, pk_user):
    content = ""
    if option == "enroll":
        enroll = Enrollment(virtualroom  = VirtualRoom.objects.get(pk=pk), user=User.objects.get(pk=pk_user), state = EnrollmentStatus.TEACHER_PENDING)
        enroll.save()
        content = "solicitada"
    if option == "enroll-pls":
        enroll  = Enrollment.objects.filter(virtualroom = VirtualRoom.objects.get(pk=pk), user=User.objects.get(pk=pk_user))
        if not enroll:
            enroll = Enrollment(virtualroom  = VirtualRoom.objects.get(pk=pk), user=User.objects.get(pk=pk_user), state = EnrollmentStatus.USER_PENDING)
            enroll.save()
        else:
            enroll.state = EnrollmentStatus.USER_PENDING
            enroll.save()
        content = "solicitada"
    
    else:
        enroll = Enrollment.objects.get(virtualroom = VirtualRoom.objects.get(pk=pk), user=User.objects.get(pk=pk_user))
        if option == "cancel":
            enroll.state= EnrollmentStatus.DISMISSED    
            content = "cancelada"
        elif option == "retired":
            enroll.state= EnrollmentStatus.RETIRED
            content = "retirada"
        elif option =="expulsed":
            enroll.state= EnrollmentStatus.EXPELLED
            content = "retirada por el profesor"
        elif option == "enrollagain":
            enroll.state= EnrollmentStatus.TEACHER_PENDING
            content = "solicitada otra vez"

        elif option == "accept":
            enroll.state= EnrollmentStatus.ACCEPTED
            content = "aprobada"
        if option == "to-student" or option == "to-teacher":
            
            if option == "to-student":
                enroll.rol = EnrollmentRols.STUDENT
            elif option == "to-teacher":
                enroll.rol = EnrollmentRols.TEACHER
            enroll.save()
            messages.success(request, f"Ahora @{enroll.user.username} es {enroll.get_rol_display()}." )
            return redirect("virtualroomdetail", pk=pk)
        enroll.save()
    messages.success(request, f"La inscripción a la clase ha sido {content} satisfactioramente." )
    return redirect("virtualroomdetail", pk=pk)

@login_required
def virtual_room_enroll(request, pk):
    vr = VirtualRoom.objects.get(pk=pk)
    context = {
        "virtualroom": vr,
        
    }
    enrollment = Enrollment.objects.filter(user=request.user, virtualroom= vr).first()
    if request.user == vr.creator:
        context["enrollmentStatus"] = "Gestionar"
    elif not enrollment:
        context["enrollmentStatus"] = "No matriculado"
    elif enrollment.state == EnrollmentStatus.ACCEPTED:
        context["enrollmentStatus"] = "Ya eres miembro"
    elif enrollment.state == EnrollmentStatus.DISMISSED:
        context["enrollmentStatus"] = "Solicitud rechazada"
    elif enrollment.state == EnrollmentStatus.TEACHER_PENDING:
        context["enrollmentStatus"] = "Solicitud pendiente de que la acepten"
    elif enrollment.state == EnrollmentStatus.USER_PENDING:
        context["enrollmentStatus"] = "Solicitud pendiente de que la aceptes"
    elif enrollment.state == EnrollmentStatus.EXPELLED:
        context["enrollmentStatus"] = "Expulsado del grupo"
    elif enrollment.state == EnrollmentStatus.RETIRED:
        context["enrollmentStatus"] = "Abandonastes del grupo"
    else:
        context["enrollmentStatus"] = "Algo extraño pasó, revisa por favor."
    
    context["enrollment"] = enrollment
    if request.method == "POST":
        search = request.POST.get("search")
        results = User.objects.filter(Q(username__icontains= search) | Q(first_name__icontains=search) | Q(last_name__icontains=search) | Q(email__icontains=search)).all()
        userWithoutEnrolled = []
        for result in results:
            # verificar que los resultados sean personas que SEAN no matriculadas, expulsadas o que no sean la creadora de la sala virtual
            
            if (not result.enrollments.filter(virtualroom = vr) or result.enrollments.filter(virtualroom=vr, state = EnrollmentStatus.EXPELLED)) and not result.virtualroomscreated.filter(pk=pk):
                userWithoutEnrolled.append(result)

        context["resultsSearch"] = userWithoutEnrolled
    context["isactive"] = "virtualroomenroll"
    return render(request, "virtualroom/search_students.html", context)