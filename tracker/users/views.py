from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.shortcuts import render
from .models import Profile, Images, Certificate
from .forms import ImageForm



# Create your views here.

def indexView(request):
    return render(request, 'index.html')

#Fovides data from backend to html templates
@login_required
def dashboardView(request):
    profile = Profile.objects.all()
    images  = Images.objects.all()
    form = ImageForm(request.POST, request.FILES)

    #context = {'profiles': profile, 'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.instance.profile = request.user.profile
            form.save()
            # img_obj = form.instance
            # return render(request, 'dashboard.html', {'images': images, 'profiles': profile, 'form': form, 'img_obj': img_obj})
            return redirect("dashboard")
    else:
        form = ImageForm()           
    return render(request, 'dashboard.html', {'form': form, 'profiles': profile, 'images': images})


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

