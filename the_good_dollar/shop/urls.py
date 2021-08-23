from django.urls import path

from .views import home_screen, load_products

app_name = 'shop'

urlpatterns = [
    path('', home_screen, name='home-screen'),
    path('products/data/<int:num>/', load_products, name='products-data'),
]
