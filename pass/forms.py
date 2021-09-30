from django import forms
from django.db.models import fields
from django.forms.models import Model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class PassForm(ModelForm):
    class Meta:
        Model = passlist
        fields = ['email_acc','username_acc','password_acc']

class RegistrationForm(UserCreationForm):
    class Meta:
        Model = User
        fields = ['username','email','password1','password2']
