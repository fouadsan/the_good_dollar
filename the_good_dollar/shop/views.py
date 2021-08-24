from django.shortcuts import render
from django.http import JsonResponse
import json
from django.db.models import Max

from .models import Subcategory, Product, Brand, Size, Color, ProductAttribute
from .utils import get_object

# Shop Home 
def home_screen(request):
    subcategories = Subcategory.objects.all()
    brands = Brand.objects.all()
    sizes = Size.objects.all()
    colors = Color.objects.all()
    max_price = ProductAttribute.objects.aggregate(Max('price'))

    context = {
        'subcategories': subcategories,
        'brands': brands,
        'sizes': sizes,
        'colors': colors,
        'max_price': max_price
    }

    return render(request, 'shop/home_screen.html', context)
    

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
                                subcategory__category_id=f_id)
                            get_object(qs, data)
                        if (filter_id.startswith("sub")):
                            qs = Product.objects.filter(
                                subcategory_id=f_id)
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


# Product detail
def product_screen(request, slug, _id):
    qs = Product.objects.get(id=_id)

    return render(request, 'shop/product_screen.html', {'qs': qs})


def add_to_cart(request):
    cart_p={}
    cart_p[str(request.GET['id'])]={
		'image':request.GET['image'],
		'title':request.GET['title'],
        'quantity': request.GET['quantity'],
		'price':request.GET['price'],
	}

    if 'cartdata' in request.session:
        if str(request.GET['id']) in request.session['cartdata']:
            cart_data=request.session['cartdata']
            cart_data[str(request.GET['id'])]['quantity']=int(cart_p[str(request.GET['id'])]['quantity'])
            cart_data.update(cart_data)
            request.session['cartdata']=cart_data
        else:
            cart_data=request.session['cartdata']
            cart_data.update(cart_p)
            request.session['cartdata']=cart_data
    else:
        request.session['cartdata']=cart_p

    return JsonResponse({'data':request.session['cartdata'],'totalitems':len(request.session['cartdata'])})
