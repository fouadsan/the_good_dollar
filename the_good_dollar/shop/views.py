from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import Category, Subcategory, Product, Brand, Size, Color
from .utils import get_object


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

    # Filters
    filter_request = request.GET.get('filters-data')

    try:

        filter_ids = json.loads(filter_request)

        if filter_ids:
            for filter_id in filter_ids:
                f_id = filter_id.split('-')[1]
                if (filter_id.startswith("cat")):
                    qs = Product.objects.filter(
                        category_id=f_id)

                elif (filter_id.startswith("brd")):
                    qs = Product.objects.filter(brand_id=f_id)

                elif (filter_id.startswith("sz")):
                    qs = Product.objects.filter(
                        productattribute__size__id=f_id)

                elif (filter_id.startswith("col")):
                    qs = Product.objects.filter(
                        productattribute__color__id=f_id)

                get_object(qs, data)

    except TypeError:
        get_object(qs, data)

    if (size >= upper):
        response = {
            'data': data[lower:upper],
            'size': size
        }
    else:
        response = {
            'data': data,
            'size': size
        }
    return JsonResponse(response)
