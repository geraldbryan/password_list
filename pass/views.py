from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method = "POST":
        form = RegistrationForm(request.Post)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your account has been created! You are now able to log in')
    else:
        form = RegistrationForm()
   
    return render(request, 'pass/register.html', {'form': form})

def passlist(request):
    if request.method = "POST":
        form = PassForm()
        user = request.user.id
        if form.is_valid():
            form.save()
     
    return render(request, 'pass/post_form.html', {'form': form})


    


