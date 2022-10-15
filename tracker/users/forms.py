from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Images, Certificate

#Registartion form to render in html
class UserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )

    # Since username, password1, password2 are standard Django forms
    # We need to create a __init__ function to bootstrapify the fields 
    def __init__ (self, *args, **kwargs):
        super(UserForm, self).__init__( *args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        

#Upload form to render in html
class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Images
        fields = ('image_name', 'images')