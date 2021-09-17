import json

from django.shortcuts import render, redirect
from django.http import JsonResponse

from shop.models import Product
from shop.utils import get_object


def home_screen(request):
    return render(request, 'main/home_screen.html')


# Load Featured Prouducts:
def load_featured_products(request):
    data = []
    if request.is_ajax():
        featured_products = Product.objects.filter(is_featured=True)
        get_object(request, featured_products, data)
        response = {
            'data': data,
            'size': 1
        }
        return JsonResponse(response)
    return redirect('main:home-screen')
