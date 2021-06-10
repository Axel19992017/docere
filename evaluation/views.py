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
    if request.method == "POST":
        name = request.POST.get("name")
        description =  request.POST.get("description")
        
        evaluation = Evaluation.objects.get(pk=pk_e)
        evaluation.name = name
        evaluation.description = description
        evaluation.save()
        messages.info(request, "Evaluación editada correctamente :D")
    return redirect("virtualroomdetail", pk=evaluation.virtualroom.pk)

def delete_evaluation(request, pk_e):
    evaluation = Evaluation.objects.get(pk=pk_e)
    pk_vr = evaluation.virtualroom.pk
    evaluation.delete()
    messages.error(request, "Evaluación eliminada correctamente :D")
    return redirect("virtualroomdetail", pk=pk_vr)

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

def update_puntuation(request, pk_p):
    if request.method == "POST":
        puntuation = Puntuation.objects.get(pk=pk_p)
        amount = request.POST.get("amount")
        observation = request.POST.get("observation")
        puntuation.amount = amount
        puntuation.observation= observation    
        puntuation.save()
        messages.warning(request, f"@{puntuation.enrollment.user.username} ha sido calificado (otra vez) ")
    
    return redirect("virtualroomdetail", pk=puntuation.evaluation.virtualroom.pk)

def delete_puntuation(request, pk_p):
    puntuation = Puntuation.objects.get(pk=pk_p)
    pk_vr = puntuation.evaluation.virtualroom.pk
    puntuation.delete()
    messages.error(request, "Puntuación eliminada correctamente :D")
    return redirect("virtualroomdetail", pk=pk_vr)