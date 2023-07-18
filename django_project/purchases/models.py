from django.db import models
from django.utils import timezone

from books.models import Book
from users.models import User


class Purchase(models.Model):
    user = models.ForeignKey(User, related_name='user_purchases', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='book_purchases', on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(null=False, default=timezone.now)

    class Meta:
        db_table = 'purchase'
        ordering = ('-purchase_date', )
