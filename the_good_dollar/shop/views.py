from django.shortcuts import redirect, render
from django.http import JsonResponse
import json
from django.db.models import Max

from .models import Subcategory, Product, Brand, Size, Color, ProductAttribute
from .utils import get_object, add_to_cart_or_fav, delete_or_update_from_cart_or_fav, get_items

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
    if request.is_ajax():  
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
    return redirect('shop:home-screen')


# Product Detail
def product_screen(request, slug, _id):
    qs = Product.objects.get(id=_id)
    return render(request, 'shop/product_screen.html', {'qs': qs})


# Add Product To Cart
def add_to_cart(request):
    if request.is_ajax():
        return add_to_cart_or_fav(request, "cart_data")
    return redirect('shop:home-screen')


# Delete Product From Cart
def delete_or_update_cart_item(request):
    if request.is_ajax():
        return delete_or_update_from_cart_or_fav(request, "cart_data", "delete")
    return redirect('shop:home-screen')


# Cart Page
def cart_screen(request):
    context = get_items(request, "cart_data")
    return render(request, 'shop/cart_screen.html',context)

# Add Product To Wishlist
def add_to_wishlist(request):
    if request.is_ajax():
        return add_to_cart_or_fav(request, "wishlist_data")
    return redirect('shop:home-screen')


# Delete Product From Fav
def delete_or_update_wishlist_item(request):
    if request.is_ajax():
        return delete_or_update_from_cart_or_fav(request, "wishlist_data", "update")
    return redirect('shop:home-screen')

