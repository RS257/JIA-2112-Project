from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Images, Certificate

#Registartion form to render in html
class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )

#Upload form to render in html
class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Images
        fields = ('image_name', 'images')