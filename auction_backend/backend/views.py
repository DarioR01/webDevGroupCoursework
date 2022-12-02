import json
from types import SimpleNamespace
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from backend.models import User
from django.contrib.auth.models import User as Django_User
from django.contrib.auth import authenticate

def create_user(user):
    username = user.email
    email = user.email
    password = user.password

    new_user = Django_User.objects.create_user(username, email, password)
    new_user.save()


@csrf_exempt 
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))

        user = User.objects.create(
            email         = data.email,
            name          = data.name,
            surname       = data.surname,
            # date_of_birth = data.date_of_birth,
            password      = data.password,

        )

        user.save()

        user = User.objects.get(pk = user.id)

        try:
            user.image = data.image
            user.save()
        except: pass

        create_user(user)

        # TODO: there is a bug when returning new_user.to_dict(). Even when image field is removed from 
        # to_dict() in models, it still outputs Object of type ImageFieldFile is not JSON serializable
        # not sure what is throwing this
        
        return JsonResponse(user.id, safe=False)

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


def authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is not None:
        return True
    return False
