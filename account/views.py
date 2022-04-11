from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from account.forms import LoginForm, RegisterForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

def loginView(request):
    next = request.GET.get('next', '/')
    print('========>', next)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username = form.cleaned_data.get('username'), password = form.cleaned_data.get('password'))
            if user is not None:
                login(request = request, user = user)
                return redirect(next)
                return redirect(reverse_lazy('index'))
    context = {
        'forms': LoginForm()
    }
    return render(request, 'login.html', context)    

def logoutView(request):
    logout(request)
    return redirect(reverse_lazy('login'))

def registerView(request):
    if request.method == 'POST':
        user = RegisterForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect(reverse_lazy('login'))        
            
        messages.add_message(request, messages.ERROR, 'error yarandi')

    context = {
        'forms': RegisterForm()
    }
    return render(request, 'register.html', context=context)


@login_required
def profileView(request):
    return HttpResponse('<h1>Profile page</h1>')