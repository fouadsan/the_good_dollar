from django.http import JsonResponse

def get_object(qs, data):
    try: 
        for obj in qs:
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
                'image': obj.productattribute_set.first().image.url
            }
            if item not in data:
                data.append(item)

    except Exception as e:
        raise Exception(e)


def add_to_cart_or_fav(request, element):
    del request.session[f'{element}']
    element_p = {}
    element_p[str(request.GET['id'])] = {
		'image':request.GET['image'],
		'title':request.GET['title'],
        'quantity': request.GET['quantity'],
		'price':request.GET['price'],
	}

    if f'{element}' in request.session:
        if str(request.GET['id']) in request.session[f'{element}']:
            element=request.session[f'{element}']
            element[str(request.GET['id'])]['quantity'] = int(element_p[str(request.GET['id'])]['quantity'])
            element.update(element)
            request.session[f'{element}'] = element
        else:
            element=request.session[f'{element}']
            element.update(element_p)
            request.session[f'{element}'] = element
    else:
        request.session[f'{element}'] = element_p

    return JsonResponse({'data': request.session[f'{element}'],'total_items': len(request.session[f'{element}'])})


def delete_from_cart_or_fav(request, element):
    p_id=str(request.GET['id'])
    if f'{element}' in request.session:
        if p_id in request.session[f'{element}']:
            cart_data=request.session[f'{element}']
            del request.session[f'{element}'][p_id]
            request.session[f'{element}']=cart_data
    total_amt=0
    for p_id,item in request.session[f'{element}'].items():
        total_amt+=int(item['quantity'])*float(item['price'])

    data = {
        f'{element}': request.session[f'{element}'],
        'total_items': len(request.session[f'{element}']),
        'total_amt': total_amt
    }

    return JsonResponse({'data': data})


def get_items(request, element):
    total_amt=0
    
    if f'{element}' in request.session:
        print(element)
        for p_id, item in request.session[f'{element}'].items():
            total_amt+=int(item['quantity'])*float(item['price'])
        context = {
            f'{element}': request.session[f'{element}'],
            'total_items': len(request.session[f'{element}']),
            'total_amt': total_amt
        }
        
    else:

        context = {
            f'{element}': '',
            'total_items': 0,
            'total_amt': total_amt,
        }

    return context