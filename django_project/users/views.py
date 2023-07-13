from django.http import HttpResponse
from django.shortcuts import render


def users_greeting(request):
    return HttpResponse('Hello, users!')
