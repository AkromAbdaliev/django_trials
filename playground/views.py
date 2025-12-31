from django.shortcuts import render
from django.http import HttpResponse


def greeting(request) -> HttpResponse:
    return render(request, 'index.html', {'name': 'Cybernetic'})
