import json

from django.http import HttpResponse

from books.models import Book


def books_json(request):
    books = Book.objects.all()
    data = [{'id': book.id,
             'title': book.title,
             'author': book.author,
             'price': book.price}
            for book in books]
    json_data = '\n'.join(json.dumps(book) for book in data)
    return HttpResponse(json_data, content_type='application/json')
