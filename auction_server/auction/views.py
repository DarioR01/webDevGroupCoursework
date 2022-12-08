from types import SimpleNamespace
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect, Http404, HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout

import json
from .forms import UserRegistration, UserLogin
from typing import Dict
from datetime import datetime
from .utils import *

from .models import User, Item

def user_login(request: HttpRequest):
    if request.method == 'POST':
        form: UserLogin = UserLogin(request.POST)
        if form.is_valid():
            email:str = form.cleaned_data['email']
            password:str = form.cleaned_data['password']

            user: User = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect('http://localhost:5173/')
                response.set_cookie('login', 'true') 
                return response
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
        logout(request)
        response= HttpResponse()
        response.delete_cookie('login')
        return response
    return Http404()

def item_page(request: HttpRequest, item_id:int):
    if request.method == 'GET':
        try:
            item: Item = get_item(item_id)
        except: 
            return HttpResponseBadRequest("No item found")

        
        owner: User = get_user(item.owner.id)
        owner = owner.to_dict()

        # if there is a bidder, get details of highest bidder
        highest_bidder: User
        try:
            highest_bidder= get_user(item.highest_bidder.id)
            highest_bidder = highest_bidder.to_dict()
        except: 
            highest_bidder = {}


        # construct payload object with info about item, bidderm owner
        payload : Dict[str][any] = {
            "id": item.id,
            "title": item.title,
            "description": item.description,
            "price": item.price,
            "highest_bidder": highest_bidder,
            "owner": owner
        }

        return JsonResponse(payload)