from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


def greeting(request) -> HttpResponse:
    query_set = Product.objects.values_list('id', 'title', 'collection__title')
    return render(request, 'index.html', {'name': 'Cybernetic', 'products': list(query_set)})
