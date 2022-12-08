from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistration, UserLogin
from typing import Dict
from datetime import datetime

from .models import User

def user_login(request: HttpRequest):
    if request.method == 'POST':
        form: UserLogin = UserLogin(request.POST)
        if form.is_valid():
            email:str = form.cleaned_data['email']
            password:str = form.cleaned_data['password']

            user: User = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('http://localhost:5173/')
            return Http404()
    else:
        form : UserLogin = UserLogin()

    return render(request, 'auth/login.html', {'form': form})

def registration(request: HttpRequest):
    if request.method == 'POST':
        form: UserRegistration = UserRegistration(request.POST)
        if form.is_valid():
            name:str = form.cleaned_data['name']
            surname:str = form.cleaned_data['surname']
            email:str = form.cleaned_data['email']
            password:str = form.cleaned_data['password']
            date:datetime = form.cleaned_data['date']

            user: Dict[str, str]= User.objects.create(
                email = email,
                name = name,
                surname = surname,
                date_of_birth = date,
            )
            user.set_password(password)
            user.save()
            return HttpResponseRedirect('/login/')
    else:
        form: UserRegistration = UserRegistration()

    return render(request, 'auth/registration.html', {'form': form})

def user_logout(request: HttpRequest):
    if request.method == 'POST':
        print("Ok")
        logout(request)
        return HttpResponse()
    return Http404()