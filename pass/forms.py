from django import forms
from django.db.models import fields
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class PassForm(ModelForm):
    class Meta:
        model = passlist
        fields = ['account_type','application_name','email','username','password']

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
