from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.shortcuts import render
from .models import Profile, Images, Certificate
from .forms import ImageForm
from django.utils import timezone

def indexView(request):
    return render(request, 'index.html')

#Fovides data from backend to html templates
@login_required
def dashboardView(request):
    profile = Profile.objects.all()
    images  = Images.objects.all()
    form = ImageForm(request.POST, request.FILES)

    if request.method == 'POST':
        if form.is_valid():
            form.instance.profile = request.user.profile
            form.instance.certification_due_date =  form.instance.getDueDate()
            form.instance.is_valid = form.instance.isValid()
            form.save()
            return redirect("dashboard")
    else:
        form = ImageForm()           
    return render(request, 'dashboard.html', {'form': form, 'profiles': profile, 'images': images})  

#Provides data from backend to html templates
def registerView(request):
    if request.method == "POST":
        form = UserForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserForm()    
    return render(request, 'registration/register.html', {'form': form }) 

