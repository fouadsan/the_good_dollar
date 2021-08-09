from django.shortcuts import render
from django.http import JsonResponse

from .models import Product


def home(request):
    return render(request, 'shop/shop.html', {'title': 'Shop'})


def load_products(request):
    qs = Product.objects.all()
    data = []
    for obj in qs:
        item = {
            'id': obj.id,
            'title': obj.title,
            'slug': obj.slug,
            'detail': obj.detail,
            'specs': obj.specs,
            'category': obj.category.title,
            'category_color': obj.category.color_code,
            'brand': obj.brand.title,
            'status': obj.status,
            'is_featured': obj.is_featured,
            'price': obj.productattribute_set.first().price,
            'image': obj.productattribute_set.first().image.url
        }
        data.append(item)

    response = {
        'data': data
    }
    return JsonResponse(response)
