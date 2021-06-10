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

def edit_topic(request, pk_t):
    topic = Topic.objects.get(pk=pk_t)
    if request.method == "POST":
        form = TopicModelForm(request.POST)
        
        files = request.FILES.getlist('file')
        if form.is_valid():
            topic_instance = form.save(commit=False)
            topic.name = topic_instance.name
            topic.description = topic_instance.description
            topic.save()

        else:
            messages.error(request, "Sucedió algo, pongase a llorar por favor")
        return redirect("virtualroomdetail", pk = topic.section.virtualroom.pk)
    else:
        # https://stackoverflow.com/questions/11667845/object-has-no-attribute-get
        form = TopicModelForm(instance = topic)
        context ={
            "TopicForm": form,
            "topic": topic,
        }
        return render(request, "virtualroom/topic_form.html", context)


def delete_topic(request, pk_t):
    topic = Topic.objects.get(pk=pk_t)
    
    topic.delete()
    messages.info(request, "Se ha eliminado el tema.")
    return redirect("virtualroomdetail", pk = topic.section.virtualroom.pk)

def delete_sections(request, pk_s):
    section = Section.objects.get(pk=pk_s)
    
    section.delete()
    messages.info(request, "Se ha eliminado el tema.")
    return redirect("virtualroomdetail", pk = section.virtualroom.pk)

            
def create_section(request):
    if request.method == "POST":
        vr = VirtualRoom.objects.get(pk=int(request.POST.get("pk_vr")))
        name = request.POST.get("name")
        section = Section(name = name, virtualroom = vr).save()
        messages.success(request, "Sección creada satisfactoriamente")
        return redirect("virtualroomdetail", pk = vr.pk)
    else:
        return redirect("virtualrooms")

def edit_sections(request, pk_s):
    if request.method == "POST":
        
        name = request.POST.get("name")
        section = Section.objects.get(pk=pk_s)
        section.name = name
        section.save()
        messages.success(request, "Sección creada satisfactoriamente")
        return redirect("virtualroomdetail", pk = section.virtualroom.pk)
    else:
        return redirect("virtualrooms")
