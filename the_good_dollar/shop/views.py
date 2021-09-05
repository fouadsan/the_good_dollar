from django.shortcuts import redirect, render
from django.http import JsonResponse
import json
from django.db.models import Max, Avg

from .models import Subcategory, Product, Brand, Size, Color, ProductAttribute, ProductReview
from .forms import ReviewForm
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
    data = []
    if request.is_ajax():
        visible = 3
        qs = Product.objects.all()
        upper = num
        lower = upper - visible
        
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
                                get_object(request, qs, data)
                            if (filter_id.startswith("sub")):
                                qs = Product.objects.filter(
                                    subcategory_id=f_id)
                                get_object(request, qs, data)
                            
                            elif (filter_id.startswith("brd")):
                                qs = Product.objects.filter(brand_id=f_id)
                                get_object(request, qs, data)

                            elif (filter_id.startswith("sz")):
                                qs = Product.objects.filter(
                                    productattribute__size__id=f_id)
                                get_object(request, qs, data)

                            elif (filter_id.startswith("col")):
                                qs = Product.objects.filter(
                                    productattribute__color__id=f_id)
                                get_object(request, qs, data)

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
                    get_object(request, qs, data)

                except TypeError:
                    pass

            size = len(data)

        get_object(request, qs, data)
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
    review_form = ReviewForm(request.POST or None)
    qs = Product.objects.get(id=_id)
    colors = ProductAttribute.objects.filter(product=qs).values('color__id','color__title','color__color_code').distinct()
    sizes = ProductAttribute.objects.filter(product=qs).values('size__id','size__title','price','color__id').distinct()

    # Check
    canAdd = True
    reviewCheck = ProductReview.objects.filter(user=request.user,product = qs).count()
    if request.user.is_authenticated:
        if reviewCheck > 0:
            canAdd = False
    # End

    # Fetch reviews
    reviews = ProductReview.objects.filter(product=qs)
    # End

    # Fetch avg rating for reviews
    avg_reviews = ProductReview.objects.filter(product = qs).aggregate(avg_rating=Avg('review_rating'))
    # End
    

    

    context = {
        'qs': qs,
        'sizes': sizes,
        'colors': colors,
        'canAdd': canAdd,
        'reviews': reviews,
        'avg_reviews': avg_reviews,
        'review_form': review_form
    } 

    return render(request, 'shop/product_screen.html', context)


# Add Product Review
def add_review(request):
    review_form = ReviewForm(request.POST or None)
    if  request.is_ajax():
        p_id = request.POST.get('id')
        qs = Product.objects.get(id=p_id)
        instance = review_form.save(commit=False)
        instance.product = qs
        instance.user = request.user
        instance = review_form.save()

        data = {
            'user': instance.user.username,
            'review_text': instance.review_text,
            'review_rating': instance.review_rating,
        }

        # Fetch avg rating for reviews
        avg_reviews = ProductReview.objects.filter(product = qs).aggregate(avg_rating=Avg('review_rating'))
	    # End

        return JsonResponse({
            'data': data,
            'avg_reviews': avg_reviews
            })


# Load Related Prouducts:
def load_related_products(request):
    data = []
    if request.is_ajax():
        p_id = json.loads(request.GET['filters-data'])
        qs = qs = Product.objects.get(id=p_id)
        related_products = Product.objects.filter(subcategory=qs.subcategory).exclude(id=p_id)[:4]
        get_object(request, related_products, data)
        response = {
            'data': data,
            'size': 1   
        }
        return JsonResponse(response)
    return redirect('shop:home-screen')

# Add Product To Cart
def add_to_cart(request):
    if request.is_ajax():
        return add_to_cart_or_fav(request, "cart_data")
    return redirect('shop:home-screen')


# Delete Product From Cart
def delete_cart_item(request):
    if request.is_ajax():
        return delete_or_update_from_cart_or_fav(request, "cart_data", "delete")
    return redirect('shop:home-screen')


# Cart Page
def cart_screen(request):
    context = get_items(request, "cart_data")
    return render(request, 'shop/cart_screen.html', context)


# Update In Cart 
def update_cart_item(request):
    p_id = str(request.GET['id'])
    p_qty = request.GET['quantity']

    if 'cart_data' in request.session:
        if p_id in request.session['cart_data']:
            cart_data = request.session['cart_data']
            cart_data[str(request.GET['id'])]['quantity'] = p_qty
            request.session['cart_data'] = cart_data
    total_amt=0
    
    for p_id,item in request.session['cart_data'].items():
        total_amt += int(item['quantity']) * float(item['price'])

    data = {
        'cart_data': request.session['cart_data'],
        'total_items': len(request.session['cart_data']),
        'total_amt': total_amt
    }

    return JsonResponse({'data': data})


# Add Product To Wishlist
def add_to_wishlist(request):
    if request.is_ajax():
        return add_to_cart_or_fav(request, "wishlist_data")
    return redirect('shop:home-screen')


# Delete Product From Fav
def delete_wishlist_item(request):
    if request.is_ajax():
        return delete_or_update_from_cart_or_fav(request, "wishlist_data", "delete")
    return redirect('shop:home-screen')


# Favorites Page
def wishlist_screen(request):
    context = get_items(request, "wishlist_data")
    return render(request, 'shop/wishlist_screen.html',context)

