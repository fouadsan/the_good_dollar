def get_object(qs, data):
    for obj in qs:
        item = {
            'id': obj.id,
            'title': obj.title,
            'slug': obj.slug,
            'detail': obj.detail,
            'specs': obj.specs,
            'category': obj.category.title,
            'category_color': obj.category.color.color_code,
            'brand': obj.brand.name,
            'status': obj.status,
            'is_featured': obj.is_featured,
            'price': obj.productattribute_set.first().price,
            'image': obj.productattribute_set.first().image.url
        }
        data.append(item)
