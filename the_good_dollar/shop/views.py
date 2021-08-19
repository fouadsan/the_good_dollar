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
    print(filter_request)
    try:
        filter_ids = json.loads(filter_request)
        print(filter_ids)
        if filter_ids:
            print(filter_ids)
            for filter_id in filter_ids:
                f_id = filter_id.split('-')[1]
                if (filter_id.startswith("cat")):
                    qs = Product.objects.filter(
                        category_id=f_id)
                    get_object(qs, data)

                elif (filter_id.startswith("brd")):
                    qs = Product.objects.filter(brand_id=f_id)

                    get_object(qs, data)
    except TypeError:
        pass

        get_object(qs, data)

    response = {
        'data': data[lower:upper],
        'size': size
    }
    return JsonResponse(response)
