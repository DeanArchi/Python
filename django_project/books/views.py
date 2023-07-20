import json

from django.http import JsonResponse

from books.models import Book


def books_json(request):
    books = Book.objects.all()
    data = [{'id': book.id,
             'title': book.title,
             'author': book.author,
             'price': book.price}
            for book in books]
    return JsonResponse(data, safe=False, json_dumps_params={'indent': 4})
