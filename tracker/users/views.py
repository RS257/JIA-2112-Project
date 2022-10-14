from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.shortcuts import render, get_object_or_404
from .models import Profile, Images
from .forms import ImageForm

# Create your views here.

def indexView(request):
    return render(request, 'index.html')

#Fovides data from backend to html templates
@login_required
def dashboardView(request):
    profile = Profile.objects.all()
    form = ImageForm(request.POST, request.FILES)

    #context = {'profiles': profile, 'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'dashboard.html', {'profiles': profile, 'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm() 
    img = Images.objects.all()             
    return render(request, 'dashboard.html', {'img': img, 'form': form, 'profiles': profile})


#Fovides data from backend to html templates
def registerView(request):
    if request.method == "POST":
        form = UserForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserForm()    

    return render(request, 'registration/register.html', {'form': form })   
   
