from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, OrderItem


def greeting(request) -> HttpResponse:
    # query_set = Product.objects.values_list('id', 'title', 'collection__title')
    query_set = OrderItem.objects.values('product_id')
    return render(request, 'index.html', {'name': 'Cybernetic', 'products': list(query_set)})
