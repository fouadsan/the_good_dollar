from django.shortcuts import render
from django.http import JsonResponse

from .models import Category, Subcategory, Product, Brand, Size, Color


def home(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    brands = Brand.objects.all()
    sizes = Size.objects.all()
    colors = Color.objects.all()

    context = {
        'categories': categories,
        'subcategories': subcategories,
        'brands': brands,
        'sizes': sizes,
        'colors': colors
    }

    return render(request, 'shop/shop.html', context)


def load_products(request, num):
    visible = 3
    qs = Product.objects.all()
    upper = num
    lower = upper - visible
    size = qs.count()
    data = []
    for obj in qs:
        item = {
            'id': obj.id,
            'title': obj.title,
            'slug': obj.slug,
            'detail': obj.detail,
            'specs': obj.specs,
            'category': obj.category.title,
            'category_color': obj.category.color.color_code,
            'brand': obj.brand.name,
            'status': obj.status,
            'is_featured': obj.is_featured,
            'price': obj.productattribute_set.first().price,
            'image': obj.productattribute_set.first().image.url
        }
        data.append(item)

    response = {
        'data': data[lower:upper],
        'size': size
    }
    return JsonResponse(response)
