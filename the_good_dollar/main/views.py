import json
from django.db import models

from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import SmallPub
from shop.models import Product
from shop.utils import get_object


def home_screen(request):
    qs = SmallPub.objects.all()[:4]
    return render(request, 'main/home_screen.html', {'qs': qs})


# Load Featured Prouducts:
def load_featured_products(request):
    data = []
    new_data = []
    if request.is_ajax():
        featured_products = Product.objects.filter(is_featured=True)
        new_products = Product.objects.all()[:3]
        get_object(request, featured_products, data)
        get_object(request, new_products, new_data)
        response = {
            'data': data,
            'new_data': new_data,
            'size': 1
        }
        return JsonResponse(response)
    return redirect('main:home-screen')

