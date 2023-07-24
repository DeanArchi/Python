from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from books.models import Book


# def books_json(request):
#     books = Book.objects.all()
#     data = [{'id': book.id,
#              'title': book.title,
#              'author': book.author,
#              'price': book.price}
#             for book in books]
#     return JsonResponse(data, safe=False, json_dumps_params={'indent': 4})

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = ('title', 'author', 'price')
    success_url = reverse_lazy('books:book-list')


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    fields = ('title', 'author', 'price')

    def get_success_url(self):
        return reverse_lazy('books:book-detail', kwargs={'pk': self.object.pk})


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    context_object_name = 'book'
    success_url = reverse_lazy('books:book-list')
