from django import forms
from django.contrib.auth.forms import UserCreationForm

class StudentRegistrationForm(UserCreationForm):
    profile_image = forms.ImageField()
    bio = forms.CharField(widget=forms.Textarea)
    birthday = forms.DateField()


