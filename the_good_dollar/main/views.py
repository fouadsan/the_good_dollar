from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Banner, SmallPub, Service
from shop.models import Product
from shop.utils import get_object


def home_screen(request):
    banners = Banner.objects.all()[:4]
    smallpubs = SmallPub.objects.all()[:4]
    services = Service.objects.all()
    context = {
        'banners': banners,
        'smallpubs': smallpubs,
        'services': services,
    }
    return render(request, 'main/home_screen.html', context)


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
