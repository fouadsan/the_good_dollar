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
