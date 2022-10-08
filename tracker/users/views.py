from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from .models import Profile

# Create your views here.

def indexView(request):
    return render(request, 'index.html')

@login_required
def dashboardView(request):
    profile = Profile.objects.all()
    context = {'profiles': profile,}
    return render(request, 'dashboard.html', context)


def registerView(request):
    if request.method == "POST":
        form = UserForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserForm()    

    return render(request, 'registration/register.html', {'form': form })    
