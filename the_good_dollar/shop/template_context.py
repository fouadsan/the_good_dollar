from .models import Category

def get_context(request):
    categories = Category.objects.all()
    # del request.session["cart_data"]
    # del request.session["wishlist_data"]
    cart_data = request.session.get('cart_data', {})
    wishlist_data = request.session.get('wishlist_data', {})
    
    context = {
        'categories': categories,
        'cart_data': cart_data,
        'wishlist_data': wishlist_data,
    }

    return context