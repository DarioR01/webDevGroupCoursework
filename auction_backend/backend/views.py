import json

from typing import List, Dict
from types import SimpleNamespace

from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseBadRequest
from django.core.exceptions import BadRequest

from backend.models import User

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate


def is_email_taken(email):
    try: 
        user = User.objects.filter(email = email).get()
        if user: 
            # a user exist, this email is taken
            return True 
    except: 
        return False

@csrf_exempt 
def register(request):
    if request.method == 'POST':
        data: SimpleNamespace = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))

        if is_email_taken(data.email):
            return JsonResponse("Username already exist", safe=False)

        try:
            user: Dict[str, str]= User.objects.create(
                email         = data.email,
                name          = data.name,
                surname       = data.surname,
                date_of_birth = data.date_of_birth,
                password      = data.password,
            )
            user.save()
            return JsonResponse(user.id, safe=False)

        except:
            return HttpResponseBadRequest("A new account could not be created. Check that all fields are correct")
    

@csrf_exempt 
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))

        email         = data.email
        password      = data.password

        is_authenticated = authenticate_user(email, password)   

        if is_authenticated:     
            user = User.objects.filter(email = email).get()
            return JsonResponse(user.id, safe=False)

        ## TODO implement better error handling
        return JsonResponse("not authenticated", safe=False)


def authenticate_user(email, password):
    user = authenticate(email=email, password=password)
    if user is not None:
        return True
    return False
