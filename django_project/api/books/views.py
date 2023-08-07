from rest_framework.viewsets import ModelViewSet

from api.books.filters import BookFilter
from api.books.serializers import BookSerializer
from books.models import Book


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
    search_fields = ('title', 'author')
    ordering_fields = ('price',)
