from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length = 200) 
    gender = forms.ChoiceField(choices = GENDER)

    class Meta:
        model = User
        fields = ["username", "email", "gender", "password1", "password2"]