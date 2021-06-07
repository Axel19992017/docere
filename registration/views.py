from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import PersonalInformation
from .forms import RegisterUserForm
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
def profile(request):
    context = {}
    if not hasattr(request.user, "information"):
        context["completed"] = False
        messages.warning(request, "Aún no ha completado su perfil, por favor, hazlo pronto :D")
    else:
        context["completed"] = True
    return render(request, "accounts/profile.html", context=context)


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('username')
            user.password = form.cleaned_data.get('password')
            user.set_password(user.password)
            user.save()
            user = authenticate(username=user.username, password=form.cleaned_data.get('password'))
            
            login(request, user)
            return redirect('myprofile')


        return redirect('register')
    else:
    
        form = RegisterUserForm()
        return render(request, 'registration/register.html', {'form': form})

class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy('myprofile')


class PersonalInformationUpdate(LoginRequiredMixin, UpdateView):
    model = PersonalInformation
    fields = ['photo', 'web_page', 'ocupation', 'phone', 'facebook_link', 'twitter_link', 'instagram_link', 'linkedin_link']
    exclude = ['user']
    success_url = reverse_lazy('myprofile')


class PersonalInformationCreate(LoginRequiredMixin, CreateView):
    model = PersonalInformation
    fields = ['photo', 'web_page', 'ocupation', 'phone', 'facebook_link', 'twitter_link', 'instagram_link', 'linkedin_link']
    success_url = reverse_lazy('myprofile')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super().form_valid(form)
