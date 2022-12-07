import json

from typing import List, Dict
from types import SimpleNamespace

from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseBadRequest

from backend.models import User

from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

def is_email_taken(email: str):
    try: 
        user : User = get_user(email)
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
            return HttpResponseBadRequest({"Username already exist"}, safe=False)

        try:
            user: Dict[str, str]= User.objects.create(
                email = data.email,
                name = data.name,
                surname = data.surname,
                #date_of_birth = data.date_of_birth,
            )
            user.set_password(data.password)
            user.save()
            return JsonResponse(user.id, safe=False)

        except:
            return HttpResponseBadRequest({"A new account could not be created. Check that all fields are correct"}, safe=False)

def get_user(email:str):
    user: User = User.objects.filter(email=email).get()
    return user

def get_auth_token(email:str):
    user: User = get_user(email)
    token = Token.objects.filter(user=user).get()
    return token


@csrf_exempt 
def login(request: HttpRequest):
    if request.method == 'POST':
        data: SimpleNamespace = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))

        email:str= data.email
        password:str= data.password

        is_user: User = is_user_authenticated(email, password)

        if is_user:
            user_name: str = is_user.to_dict().get("name") 
            user_surname: str  = is_user.to_dict().get("surname")
            token:Token = Token.objects.create(user= is_user) # Generates Token given a use.
            print(type(token)) 
            return JsonResponse({"token": token.key, "name": user_name, "surname": user_surname}, safe=False)


        return HttpResponseBadRequest({"Could not authenticate. Check that credentials are correct"}, safe=False)

@csrf_exempt 
def logout(request: HttpRequest):
    if request.method == 'POST':
        data: SimpleNamespace = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))
        email:str = data.email

        token:Token = get_auth_token(email)
        token.delete()

        return HttpResponse({"Successfully logged out."}, safe=False)

def is_user_authenticated(email, password):
    user: User = authenticate(email=email, password=password)
    if user is not None:
        return user # a user with those credentials exists and user object is returned
    return False
