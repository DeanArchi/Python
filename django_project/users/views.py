import json

from django.http import HttpResponse

from users.models import User


def users_json(request):
    users = User.objects.all()
    data = [{'id': user.id,
             'username': user.username,
             'first_name': user.first_name,
             'last_name': user.last_name}
            for user in users]
    json_data = '\n'.join(json.dumps(user) for user in data)
    return HttpResponse(json_data, content_type='application/json')
