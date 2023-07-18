import json

from django.http import HttpResponse
from django.shortcuts import render

from purchases.models import Purchase


def purchases_json(request):
    purchases = Purchase.objects.select_related('user', 'book').values(
        'id',
        'user__first_name',
        'user__last_name',
        'book__title',
        'book__price',
        'purchase_date'
    )
    data = [{"purchase_id": purchase['id'],
             'first_name': purchase['user__first_name'],
             'last_name': purchase['user__last_name'],
             'title': purchase['book__title'],
             'price': purchase['book__price'],
             'purchase_date': purchase['purchase_date'].strftime('%Y-%m-%d %H:%M:%S')}
            for purchase in purchases]
    json_data = '\n'.join(json.dumps(purchase) for purchase in data)
    return HttpResponse(json_data, content_type='application/json')
