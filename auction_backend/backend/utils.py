from auction_backend.backend.models import User
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

def get_user(email:str):
    user: User = User.objects.filter(email=email).get()
    return user

def is_user_authenticated(email, password):
    user: User = authenticate(email=email, password=password)
    if user is not None:
        return user # a user with those credentials exists and user object is returned
    return False

def get_auth_token(email:str):
    user: User = get_user(email)
    token = Token.objects.filter(user=user).get()
    return token

def is_email_taken(email: str):
    try: 
        user : User = get_user(email)
        if user: 
            # a user exist, this email is taken
            return True 
    except: 
        return False

