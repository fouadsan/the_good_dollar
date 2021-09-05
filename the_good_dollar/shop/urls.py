from django.urls import path

from .views import home_screen, load_products, product_screen, load_related_products, add_review, add_to_cart, delete_cart_item, update_cart_item, cart_screen, add_to_wishlist,\
     delete_wishlist_item, wishlist_screen

app_name = 'shop'

urlpatterns = [
    path('', home_screen, name='home-screen'),
    path('products/data/<int:num>/', load_products, name='products-data'),
    path('<str:slug>/<int:_id>/', product_screen, name='product-screen'),
    path('load_related_products', load_related_products, name='load-related-products'),
    path('add_review', add_review, name='add-review'),
    path('add_to_cart',add_to_cart,name='add-to-cart'),
    path('delete_from_cart',delete_cart_item, name='delete-from-cart'),
    path('update_cart',update_cart_item, name='update-cart'),
    path('cart',cart_screen,name='cart-screen'),
    path('add_to_wishlist',add_to_wishlist, name='add-to-wishlist'),
    path('delete_from_wishlist',delete_wishlist_item, name='delete-from-wishlist'),
    path('wishlist',wishlist_screen,name='wishlist-screen'),
]
