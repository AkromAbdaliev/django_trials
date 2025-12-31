from django.shortcuts import render
from django.http import HttpResponse


def greeting(request) -> HttpResponse:
    return HttpResponse("Hello, from the playground!")
