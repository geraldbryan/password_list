from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
# Create your views here.

def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your account has been created! You are now able to log in')
    else:
        form = RegistrationForm()
   
    return render(request, 'pass/register.html', {'form': form})

def passform(request):
    form = PassForm()
    if request.method == "POST":
        form = PassForm(request.POST)
        userid = request.user.id
        if form.is_valid():
            type = form.cleaned_data.get('account_type')
            em = form.cleaned_data.get('email')
            app = form.cleaned_data.get('application_name')
            uname = form.cleaned_data.get('username')
            passw = form.cleaned_data.get('password')
            test = passlist(account_type=type,email = em,application_name=app, username = uname, password = passw, user_id = userid)
            test.save()
            messages.success(request,f'Your account information has been saved')
            return redirect('/')
     
    return render(request, 'pass/post.html', {"form":form})

## Social Media

def socmed(request):
    res = passlist.objects.filter(user_id = request.user.id)
    res = passlist.objects.filter(account_type = 1)
     
    return render(request, 'pass/socmed.html', {'result': res})

def socmed_detail(request, pk_passlist):
    res = passlist.objects.get(id = pk_passlist)

    return render(request, 'pass/socmed_detail.html', {'result': res})

def socmed_edit(request, pk_passlist):
    cred = passlist.objects.get(id=pk_passlist)
    form = passlist(instance=cred)

    if request.method == 'POST':
        form = PassForm(request.POST, instance=cred)
        if form.is_valid():
            form.save()
            return redirect('/') 

    return render(request, 'pass/form.html', {'form': form})

def socmed_delete(request, pk_passlist):
    cred = passlist.objects.get(id=pk_passlist)
    if request.method == 'POST':
        cred.delete()
        return redirect('/')

## Email

def email(request):
    res = passlist.objects.filter(user_id = request.user.id)
    res = passlist.objects.filter(account_type = 2)
     
    return render(request, 'pass/email.html', {'result': res})

## Bank

def bank(request):
    res = passlist.objects.filter(user_id = request.user.id)
    res = passlist.objects.filter(account_type = 3)
     
    return render(request, 'pass/bank.html', {'result': res})

## Credit card

def credcard(request):
    res = passlist.objects.filter(user_id = request.user.id)
    res = passlist.objects.filter(account_type = 4)
     
    return render(request, 'pass/credcard.html', {'result': res})

def credcard_detail(request, pk_passlist):
    res = passlist.objects.get(id = pk_passlist)

    return render(request, 'pass/credcard_detail.html', {'result': res})

def credcard_edit(request, pk_passlist):
    cred = passlist.objects.get(id=pk_passlist)
    form = passlist(instance=cred)

    if request.method == 'POST':
        form = PassForm(request.POST, instance=cred)
        if form.is_valid():
            form.save()
            return redirect('/') 

    return render(request, 'pass/form.html', {'form': form})

def credcard_delete(request, pk_passlist):
    cred = passlist.objects.get(id=pk_passlist)
    if request.method == 'POST':
        cred.delete()
        return redirect('/')
    
    context = {
        'result': cred,
    }
    return render(request, 'pass/credcard_delete.html', context) 

## Health

def health(request):
    res = passlist.objects.filter(user_id = request.user.id)
    res = passlist.objects.filter(account_type = 5)
     
    return render(request, 'pass/health.html', {'result': res})

## Trading

def trading(request):
    res = passlist.objects.filter(user_id = request.user.id)
    res = passlist.objects.filter(account_type = 6)
     
    return render(request, 'pass/trading.html', {'result': res})

## Ecommerce

def ecom(request):
    res = passlist.objects.filter(user_id = request.user.id)
    res = passlist.objects.filter(account_type = 7)
     
    return render(request, 'pass/ecom.html', {'result': res})

## Other

def other(request):
    res = passlist.objects.filter(user_id = request.user.id)
    res = passlist.objects.filter(account_type = 8)
     
    return render(request, 'pass/other.html', {'result': res})


