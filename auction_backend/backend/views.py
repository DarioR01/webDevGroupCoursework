import json
from types import SimpleNamespace
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from backend.models import User

@csrf_exempt 
def create_user(request):
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

        new_user = User.objects.get(pk = user.id)

        try:
            new_user.image = data.image
            new_user.save()
        except: pass

        # TODO: there is a bug when returning new_user.to_dict(). Even when image field is removed from 
        # to_dict() in models, it still outputs Object of type ImageFieldFile is not JSON serializable
        # not sure what is throwing this
        
        return JsonResponse(new_user.id, safe=False)
