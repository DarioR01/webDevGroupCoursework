import os

from . import database
from .models import PageView, User, Item

from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, Http404, HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistration, UserLogin

from typing import Dict 
from datetime import datetime
from .utils import *

def user_login(request: HttpRequest):
    if request.method == 'POST':
        form: UserLogin = UserLogin(request.POST)
        if form.is_valid():
            email:str = form.cleaned_data['email']
            password:str = form.cleaned_data['password']

            user: User = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                response:HttpResponse = HttpResponseRedirect('/')
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
            return HttpResponseRedirect('/bidder/api/login/')
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
    try:
        filter = request.GET["filter"]
    except:
        filter = None
    if request.method == 'GET':
        items: HttpResponseBadRequest | dict = get_list_of_items(request, filter)
        return items


def item_page(request: HttpRequest, item_id:int):
    #check that item passed in url is an item and can be retrieved
    try:
        item: Item = get_item(item_id)
    except: 
        return HttpResponseBadRequest("No item found")

    # get item for item page
    if request.method == 'GET':
        body: JsonResponse = build_response_body_for_get_item(item)
        return body

    # update item's highest bidder and new price
    if request.method == 'PUT':
        updated_item: HttpResponseBadRequest | JsonResponse = update_item_highest_bidder_and_price(request, item)
        return updated_item

    # post a new question for an item
    if request.method == 'POST':
        updated_question: HttpResponseBadRequest | JsonResponse = post_question_for_item(request, item)
        return updated_question


def question_answer(request: HttpRequest, item_id: int, question_id: int):
    if request.method == 'PUT':
        updated_question: HttpResponseBadRequest | JsonResponse = post_answer_for_question(request, item_id, question_id)
        return updated_question


def profile_page(request: HttpRequest):
    if request.method == 'GET':
        user: JsonResponse = build_response_body_for_get_user(request)
        return user

    if request.method == 'PUT':
        updated_profile: HttpResponseBadRequest | JsonResponse = updated_profile_page(request)
        return updated_profile

    if request.method == 'POST':
        #find better way to get 'multipart/form-data' value out of Content-type
        content_type: str = request.headers["Content-type"][:19]
        if content_type == "multipart/form-data":
            image_name: str = edit_user_profile_upload_image(request)
            return image_name

        else:
            new_item: Item = post_new_item(request)
            return new_item

def upload_item_image(request: HttpRequest, item_id: int):
    if request.method == 'POST':
        image_name: str = post_new_item_upload_image(request, item_id)
    return image_name





def index(request):
    """Takes an request object as a parameter and creates an pageview object then responds by rendering the index view."""
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'source/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    """Takes an request as a parameter and gives the count of pageview objects as reponse"""
    return HttpResponse("hello")
