from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


def greeting(request) -> HttpResponse:
    query_set = Product.objects.filter(title__icontains='o')
    return render(request, 'index.html', {'name': 'Cybernetic', 'products': list(query_set)})
