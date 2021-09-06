from django.http import JsonResponse


def get_object(request, qs, data):

    cart_items = {}
    wishlist_items = {}
    cart_items_ids = []
    wishlist_items_ids = []
    is_cart = False
    is_fav = False

    try:
        cart_items = get_items(request, "cart_data")
        cart_items_ids = cart_items['cart_data']
    except KeyError:
        print('KEYERROR')
    if cart_items_ids:
        cart_items_ids = list(cart_items['cart_data'].keys())

    try:
        wishlist_items = get_items(request, "wishlist_data")
        wishlist_items_ids = wishlist_items['wishlist_data']
    except KeyError:
        print('KEYERROR')

    if wishlist_items_ids:
        wishlist_items_ids = list(wishlist_items['wishlist_data'].keys())

    try:
        for obj in qs:
            if (cart_items_ids):
                for cart_item_id in cart_items_ids:
                    if obj.id == int(cart_item_id):
                        is_cart = True
                    else:
                        is_cart = False
            if (wishlist_items_ids):
                for wishlist_item_id in wishlist_items_ids:
                    if obj.id == int(wishlist_item_id):
                        is_fav = True
                    else:
                        is_fav = False
            item = {
                'id': obj.id,
                'title': obj.title,
                'slug': obj.slug,
                'detail': obj.detail,
                'specs': obj.specs,
                'subcategory': obj.subcategory.title,
                'category_color': obj.subcategory.category.color.color_code,
                'brand': obj.brand.name,
                'status': obj.status,
                'is_featured': obj.is_featured,
                'price': obj.productattribute_set.first().price,
                'image': obj.productattribute_set.first().image.url,
                'is_cart': is_cart,
                'is_fav': is_fav
            }
            if item not in data:
                data.append(item)

    except Exception as e:
        raise Exception(e)


def add_to_cart_or_fav(request, element):
    # del request.session[element]
    element_p = {}
    element_p[str(request.GET['id'])] = {
        'image': request.GET['image'],
        'title': request.GET['title'],
        'quantity': request.GET['quantity'],
        'price': request.GET['price'],
    }

    if element in request.session:
        if str(request.GET['id']) in request.session[element]:
            if element == "cart_data":
                cart_data = request.session[element]
                cart_data[str(request.GET['id'])]['quantity'] = int(
                    element_p[str(request.GET['id'])]['quantity'])
                cart_data.update(cart_data)
                request.session[element] = cart_data
            else:
                wishlist_data = request.session[element]
                wishlist_data[str(request.GET['id'])]['quantity'] = int(
                    element_p[str(request.GET['id'])]['quantity'])
                wishlist_data.update(wishlist_data)
                request.session[element] = wishlist_data
        else:
            if element == "cart_data":
                cart_data = request.session[element]
                cart_data.update(element_p)
                request.session[element] = cart_data
            else:
                wishlist_data = request.session[element]
                wishlist_data.update(element_p)
                request.session[element] = wishlist_data

    else:
        request.session[element] = element_p

    return JsonResponse({'data': request.session[element], 'total_items': len(request.session[element])})


def delete_or_update_from_cart_or_fav(request, element, action):
    total_amt = 0

    product_id = str(request.GET['id'])

    product_qty = request.GET['quantity']

    if element in request.session:
        if product_id in request.session[element]:
            if element == "cart_data":
                cart_data = request.session[element]

                if action == "delete":
                    del request.session[element][product_id]
                else:
                    cart_data[str(request.GET['id'])]['quantity'] = product_qty

                request.session[element] = cart_data

            else:
                wishlist_data = request.session[element]

                if action == "delete":
                    del request.session[element][product_id]
                else:
                    wishlist_data[str(request.GET['id'])
                                  ]['quantity'] = product_qty

                request.session[element] = wishlist_data

    for product_id, item in request.session[element].items():
        total_amt += int(item['quantity'])*float(item['price'])

    data = {
        element: request.session[element],
        'total_items': len(request.session[element]),
        'total_amt': total_amt
    }

    return JsonResponse({'data': data})


def get_items(request, element):

    total_amt = 0

    if request.session[element]:
        items = request.session[element]
    else:
        items = ''

    if element in request.session:
        for product_id, item in request.session[element].items():
            total_amt += int(item['quantity']) * float(item['price'])

    context = {
        element: items,
        'total_items': len(request.session[element]),
        'total_amt': total_amt
    }

    return context
