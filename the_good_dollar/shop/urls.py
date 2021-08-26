from django.urls import path

from .views import home_screen, load_products, product_screen, add_to_cart, delete_or_update_cart_item, cart_screen, add_to_wishlist, delete_or_update_wishlist_item

app_name = 'shop'

urlpatterns = [
    path('', home_screen, name='home-screen'),
    path('products/data/<int:num>/', load_products, name='products-data'),
    path('<str:slug>/<int:_id>/', product_screen, name='product-screen'),
    path('add_to_cart',add_to_cart,name='add-to-cart'),
    path('delete_or_update_from_cart',delete_or_update_cart_item, name='delete-or-update-from-cart'),
    path('cart',cart_screen,name='cart-screen'),
    path('add_to_wishlist',add_to_wishlist, name='add-to-wishlist'),
    path('delete_or_update_from_wishlist',delete_or_update_wishlist_item, name='delete-or-update-from-wishlist'),
]
