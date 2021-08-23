from django.shortcuts import render
from django.http import JsonResponse
import json
from django.db.models import Max

from .models import Departement, Category, Product, Brand, Size, Color, ProductAttribute
from .utils import get_object

# Shop Home 
def home_screen(request):
    departements = Departement.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    sizes = Size.objects.all()
    colors = Color.objects.all()
    max_price = ProductAttribute.objects.aggregate(Max('price'))

    context = {
        'departements': departements,
        'categories': categories,
        'brands': brands,
        'sizes': sizes,
        'colors': colors,
        'max_price': max_price
    }

    return render(request, 'shop/shop.html', context)


# Load Products
def load_products(request, num):  
    visible = 3
    qs = Product.objects.all()
    upper = num
    lower = upper - visible
    data = []

    # Filters
    filter_request = request.GET.get('filters-data')
    price_range_request = request.GET.get('price-range')
    if (filter_request or price_range_request):
        if (filter_request):
            try:
                filter_arr = json.loads(filter_request)
                if filter_arr:
                    for filter_id in filter_arr:
                        f_id = filter_id.split('-')[1]
                        if (filter_id.startswith("cat")):
                            qs = Product.objects.filter(
                                category_id=f_id)
                            get_object(qs, data)
                        
                        elif (filter_id.startswith("brd")):
                            qs = Product.objects.filter(brand_id=f_id)
                            get_object(qs, data)

                        elif (filter_id.startswith("sz")):
                            qs = Product.objects.filter(
                                productattribute__size__id=f_id)
                            get_object(qs, data)

                        elif (filter_id.startswith("col")):
                            qs = Product.objects.filter(
                                productattribute__color__id=f_id)
                            get_object(qs, data)


            except TypeError:
                pass

        elif(price_range_request):
            try:
                filter_arr = json.loads(price_range_request)
                if (filter_arr[0] <= filter_arr[1]):
                    min_price = filter_arr[0]
                    max_price = filter_arr[1]
                else:
                    min_price = filter_arr[1]
                    max_price = filter_arr[0]
                    
                qs = qs.filter(productattribute__price__gte=min_price, productattribute__price__lte=max_price)
                get_object(qs, data)

            except TypeError:
                pass

        size = len(data)

    get_object(qs, data)
    size = qs.count()

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
