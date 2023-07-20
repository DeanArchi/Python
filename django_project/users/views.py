import json

from django.http import JsonResponse

from users.models import User


def users_json(request):
    users = User.objects.all()
    data = [{'id': user.id,
             'username': user.username,
             'first_name': user.first_name,
             'last_name': user.last_name}
            for user in users]
    return JsonResponse(data, safe=False, json_dumps_params={'indent': 4})
