from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'username: {self.username}, full name: {self.first_name} {self.last_name}'

    class Meta:
        db_table = 'user'
