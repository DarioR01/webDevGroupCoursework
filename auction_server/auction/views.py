from types import SimpleNamespace
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect, Http404, HttpResponse, JsonResponse, HttpResponseBadRequest, FileResponse
from django.contrib.auth import authenticate, login, logout

import json
from .forms import UserRegistration, UserLogin
from typing import Dict 
from datetime import datetime
from .utils import *

from .models import User, Item, Question, Image

def user_login(request: HttpRequest):
    if request.method == 'POST':
        form: UserLogin = UserLogin(request.POST)
        if form.is_valid():
            email:str = form.cleaned_data['email']
            password:str = form.cleaned_data['password']

            user: User = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                response:HttpResponse = HttpResponseRedirect('http://localhost:5173/')
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
        response: HttpResponse= HttpResponse()
        response.delete_cookie('login')
        return response
    return Http404()


def home(request: HttpRequest):
    #TODO implement filetering name 'filter'
    if request.method == 'GET':
        items: Dict [any][any] = get_list_of_items(request)
        return JsonResponse(items)


def item_page(request: HttpRequest, item_id:int):
    #check that item passed in url is an item and can be retrieved
    try:
        item: Item = get_item(item_id)
    except: 
        return HttpResponseBadRequest("No item found")

    # get item for item page
    if request.method == 'GET':
        body: dict[str, str | int | User | List] = build_response_body_for_get_item(item)
        return HttpResponse(body)

    # update item's highest bidder and new price
    if request.method == 'PUT':
        updated_item: dict[str, str | int | User | List] = update_item_highest_bidder_and_price(request, item)
        return HttpResponse(updated_item)

    # post a new question for an item
    if request.method == 'POST':
        updated_question: Question = post_question_for_item(request, item)
        return HttpResponse(updated_question)


def question_answer(request: HttpRequest, item_id: int, question_id: int):
    updated_question: Question = post_answer_for_question(request, item_id, question_id)
    return JsonResponse(updated_question)

def upload_image(request: HttpRequest):
    if request.method == 'POST':
        image = request.FILES.get("file")
        image: Image = Image.objects.create(
                title = "The title",
                image = image,
            )
        image.save()
        return HttpResponse("Success. A new question was created")
    
def newItem(request: HttpRequest):
    if request.method == 'POST':
        post_new_item(request)
        return HttpResponse("Success a new item was created")
    
def getProfile(request: HttpRequest, user_id: int):
    try:
        user: User = get_user(user_id)
    except:
        return HttpResponseBadRequest("User is not found")
    
    if request.method == 'GET':
        return JsonResponse(user)
    
def editProfile(request: HttpRequest):
        if request.method == 'PUT':
            updated_profile: User = updated_profile_page(request)
            return JsonResponse(updated_profile)
