from django.shortcuts import redirect, render
from virtualroom.models import Enrollment, VirtualRoom
from .models import Evaluation
from django.contrib import messages
from evaluation.models import Puntuation

# Create your views here.
def create_evaluation(request, pk_vr):
    if request.method == "POST":
        name = request.POST.get("name")
        description =  request.POST.get("description")
        vr = VirtualRoom.objects.get(pk=pk_vr)
        evaluation = Evaluation(name=name, description=description, virtualroom= vr)
        evaluation.save()
        messages.info(request, "Evaluación creada :D")
    return redirect("virtualroomdetail", pk=pk_vr)
    

def update_evaluation(request, pk_e):
    return render(request, "")

def delete_evaluation(request, pk_e):
    return render(request, "")

def create_puntuation(request, pk_e, pk_s):
    if request.method == "POST":
        evaluation = Evaluation.objects.get(pk=pk_e)
        enrollment = Enrollment.objects.get(pk=pk_s)
        amount = request.POST.get("amount")
        observation = request.POST.get("observation")
        puntuation = Puntuation(evaluation= evaluation, enrollment=enrollment, amount=amount, observation=observation)
        puntuation.save()
        messages.success(request, f"@{enrollment.user.username} ha sido calificado ")
    
    return redirect("virtualroomdetail", pk=evaluation.virtualroom.pk)

def update_puntuation(request, pk_e, pk_s):
    return render(request, "")