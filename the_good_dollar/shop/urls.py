from django.urls import path

from .views import home_screen, load_products, product_screen, add_to_cart

app_name = 'shop'

urlpatterns = [
    path('', home_screen, name='home-screen'),
    path('products/data/<int:num>/', load_products, name='products-data'),
    path('<str:slug>/<int:_id>/', product_screen, name='product-screen'),
    path('add_to_cart',add_to_cart,name='add-to-cart'),
]
