from django.urls import path

from .views import delete_wishlist_item, home_screen, load_products, product_screen, add_to_cart, delete_cart_item, cart_screen, add_to_wishlist, delete_wishlist_item

app_name = 'shop'

urlpatterns = [
    path('', home_screen, name='home-screen'),
    path('products/data/<int:num>/', load_products, name='products-data'),
    path('<str:slug>/<int:_id>/', product_screen, name='product-screen'),
    path('add_to_cart',add_to_cart,name='add-to-cart'),
    path('delete_from_cart',delete_cart_item,name='delete-from-cart'),
    path('cart',cart_screen,name='cart-screen'),
    path('add_to_wishlist',add_to_wishlist, name='add-to-wishlist'),
    path('delete_from_wishlist',delete_wishlist_item,name='delete-from-wishlist'),
]
