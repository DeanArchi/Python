from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


@admin.register(get_user_model())
class UserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'age', 'is_staff')
