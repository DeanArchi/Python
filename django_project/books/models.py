from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=False)
    price = models.IntegerField(null=False)

    def __str__(self):
        return f'book {self.id}, title: {self.title}, author: {self.author}'

    class Meta:
        db_table = 'book'
        unique_together = ('title', 'author')
