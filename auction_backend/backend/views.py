import json

from typing import List, Dict
from types import SimpleNamespace

from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseBadRequest
from django.core.exceptions import BadRequest
from django.shortcuts import get_object_or_404

from backend.models import CustomUserManager
from backend.models import User

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate


def is_email_taken(email: str):
    try: 
        user = User.objects.filter(email = email).get()
        if user: 
            # a user exist, this email is taken
            return True 
    except: 
        return False

@csrf_exempt 
def register(request: HttpRequest):
    if request.method == 'POST':
        data: SimpleNamespace = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))

        if is_email_taken(data.email):
            return JsonResponse("Username already exist", safe=False)

        try:
            user: Dict[str, str]= User.objects.create(
                email         = data.email,
                # name          = data.name,
                # surname       = data.surname,
                # date_of_birth = data.date_of_birth,
            )
            user.set_password(data.password)
            user.save()
            return JsonResponse(user.id, safe=False)

        except:
            return HttpResponseBadRequest("A new account could not be created. Check that all fields are correct")


@csrf_exempt 
def login(request: HttpRequest):
    if request.method == 'POST':
        data: SimpleNamespace = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))

        email:str         = data.email
        password:str      = data.password

        is_user: User = is_user_authenticated(email, password)

        if is_user:
            return JsonResponse(is_user, safe=False)

        return HttpResponseBadRequest("Could not authenticate. Check that credentials are correct")


def is_user_authenticated(email, password):
    user: User = authenticate(email=email, password=password)
    if user is not None:
        return user.to_dict() # a user with those credentials exists
    return False
