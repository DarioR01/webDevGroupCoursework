from types import SimpleNamespace
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect, Http404, HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout

import json
from .forms import UserRegistration, UserLogin
from typing import Dict
from datetime import datetime
from .utils import *

from .models import User, Item, Question

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


def item_page(request: HttpRequest, item_id:int):

    try:
        item: Item = get_item(item_id)
    except: 
        except: 
    except: 
        return HttpResponseBadRequest("No item found")

    if request.method == 'GET':
        body = build_response_body_for_get_item(item)
        return JsonResponse(body)

    if request.method == 'PUT':
        try:
            item: Item = get_item(item_id)
        except: 
            return HttpResponseBadRequest("No item found")

        #TODO agree on what this fucntion is supposed to receive in the request
        
        #find the user corresponding to the highest bidder

        #update the highest bidder in the item with the highest bidder found above

        #return updated item using build_get_item_body()

        return HttpResponse("You got to this endpoint")



    

