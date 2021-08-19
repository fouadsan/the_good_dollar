from django.urls import path

from .views import home, load_products

app_name = 'shop'

urlpatterns = [
    path('', home, name='shop-home'),
    path('products/data/<int:num>/', load_products, name='products-data'),

]
