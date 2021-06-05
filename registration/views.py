from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import RegisterUserForm
# Create your views here.
def profile(request):
    return render(request, "accounts/profile.html")


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.username = form.cleaned_data.get('username')
            user.password = form.cleaned_data.get('password')
            user.set_password(user.password)
            user.save()
            user = authenticate(username=user.username, password=form.cleaned_data.get('password'))
            
            login(request, user)
            return redirect('/auth/profile/')


        return redirect('/auth/register/')
    else:
    
        form = RegisterUserForm()
        return render(request, 'registration/register.html', {'form': form})
