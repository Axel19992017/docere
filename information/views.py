from django.shortcuts import redirect, render
from .models import Document, Topic, Section
from .forms import TopicModelForm, DocumentModelForm
from virtualroom.models import VirtualRoom
from django.contrib import messages

# Create your views here.
# https://stackoverflow.com/questions/38257231/how-can-i-upload-multiple-files-to-a-model-field/52016594
def create_to_topic(request, pk_s):
    section = Section.objects.get(pk=pk_s)
    if request.method == "POST":
        form = TopicModelForm(request.POST)
        file_form = DocumentModelForm(request.POST, request.FILES)
        files = request.FILES.getlist('file')
        if form.is_valid() and file_form.is_valid():
            topic_instance = form.save(commit=False)
            topic_instance.section = section
            topic_instance.save()

            for f in files:
                file_instance = Document(file = f, topic = topic_instance)
                file_instance.save()
        else:
            messages.error(request, "Sucedió algo, pongase a llorar por favor")
        return redirect("virtualroomdetail", pk = section.virtualroom.pk)
    else:
        return redirect("virtualrooms")
            
def create_section(request):
    if request.method == "POST":
        vr = VirtualRoom.objects.get(pk=int(request.POST.get("pk_vr")))
        name = request.POST.get("name")
        section = Section(name = name, virtualroom = vr).save()
        messages.success(request, "Sección creada satisfactoriamente")
        return redirect("virtualroomdetail", pk = vr.pk)
    else:
        return redirect("virtualrooms")
