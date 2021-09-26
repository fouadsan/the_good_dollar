from django.shortcuts import redirect, render
from django.http import JsonResponse
import json
from django.db.models import Max, Avg

from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm

from .models import Subcategory, Product, Brand, Size, Color, ProductAttribute, ProductReview
from users.models import CartOrder, CartOrderItems, AddressBook
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

                    qs = qs.filter(productattribute__price__gte=min_price,
                                   productattribute__price__lte=max_price)
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
    colors = ProductAttribute.objects.filter(product=qs).values(
        'color__id', 'color__title', 'color__color_code').distinct()
    sizes = ProductAttribute.objects.filter(product=qs).values(
        'size__id', 'size__title', 'price', 'color__id').distinct()

    # Check
    can_add = True
    reviewCheck = ProductReview.objects.filter(
        user=request.user, product=qs).count()
    if request.user.is_authenticated:
        if reviewCheck > 0:
            can_add = False
    # End

    # Fetch reviews
    reviews = ProductReview.objects.filter(product=qs)
    # End

    # Fetch avg rating for reviews
    avg_reviews = ProductReview.objects.filter(
        product=qs).aggregate(avg_rating=Avg('review_rating'))
    # End

    context = {
        'qs': qs,
        'sizes': sizes,
        'colors': colors,
        'can_add': can_add,
        'reviews': reviews,
        'avg_reviews': avg_reviews,
        'review_form': review_form
    }

    return render(request, 'shop/product_screen.html', context)


# Search
def search(request):
    if request.is_ajax():
        res = None
        product = request.POST.get('product')
        category_id = request.POST.get('category_id')
        print(category_id)
        if category_id:
            qs = Product.objects.filter(title__icontains=(product)).filter(subcategory__category_id=category_id)
        else:
            qs = Product.objects.filter(title__icontains=(product))

        if len(qs) > 0 and len(product) > 0:
            data = []
            for obj in qs:
                item = {
                    'id': obj.id,
                    'title': obj.title,
                    'slug': obj.slug,
                    'image': obj.productattribute_set.first().image.url
                }
                data.append(item)
            res = data
        else:
            res = 'No Product Found ...'

        return JsonResponse({'resp': res})

    return redirect('shop:home-screen')

# Add Product Review


def add_review(request):
    review_form = ReviewForm(request.POST or None)
    if request.is_ajax():
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
        avg_reviews = ProductReview.objects.filter(
            product=qs).aggregate(avg_rating=Avg('review_rating'))
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
        related_products = Product.objects.filter(
            subcategory=qs.subcategory).exclude(id=p_id)[:4]
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
    total_amt = 0

    for p_id, item in request.session['cart_data'].items():
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
    return render(request, 'shop/wishlist_screen.html', context)


# Checkout
def checkout_screen(request):
    total_amt = 0
    totalAmt = 0

    if 'cart_data' in request.session:
        for p_id, item in request.session['cart_data'].items():
            totalAmt += int(item['quantity']) * float(item['price'])
        # Order
        order = CartOrder.objects.create(
            user=request.user,
            total_amt=totalAmt
        )
        # End
        for p_id, item in request.session['cart_data'].items():
            total_amt += int(item['quantity']) * float(item['price'])
            # OrderItems
            items = CartOrderItems.objects.create(
                order=order,
                invoice_no='INV-'+str(order.id),
                item=item['title'],
                image=item['image'],
                quantity=item['quantity'],
                price=item['price'],
                total=float(item['quantity']) * float(item['price'])
            )
            # End
        # Process Payment
        host = request.get_host()
        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': total_amt,
            'item_name': 'OrderNo-' + str(order.id),
            'invoice': 'INV-' + str(order.id),
            'currency_code': 'USD',
            'notify_url': 'http://{}{}'.format(host, reverse('shop:paypal-ipn')),
            'return_url': 'http://{}{}'.format(host, reverse('shop:payment-done')),
            'cancel_return': 'http://{}{}'.format(host, reverse('shop:payment-cancelled')),
        }
        form = PayPalPaymentsForm(initial=paypal_dict)
        address = AddressBook.objects.filter(
            user=request.user, status=True).first()

    context = {
        'cart_data': request.session['cart_data'],
        'total_items': len(request.session['cart_data']),
        'total_amt': total_amt,
        'form': form,
        'address': address
    }
    return render(request, 'shop/checkout_screen.html', context)


@csrf_exempt
def payment_done(request):
    return_data = request.POST
    return render(request, 'shop/payment_success.html', {'data': return_data})


@csrf_exempt
def payment_canceled(request):
    return render(request, 'shop/payment_fail.html')
