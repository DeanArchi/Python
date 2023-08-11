from celery import shared_task

from purchases.models import Purchase
from users.models import User


@shared_task
def print_something():
    print('=====USER HAS OPENED A USERS LIST=====')


@shared_task
def purchases_of_user(user_id):
    purchase_count = Purchase.objects.filter(user_id=user_id).count()
    print(f'User ID: {user_id}, Number of purchases: {purchase_count}')


@shared_task
def print_quantity_of_users():
    users_count = User.objects.count()
    print(f'Quantity of users in database: {users_count}')
