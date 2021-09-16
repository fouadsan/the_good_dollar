from django.urls import path

from .views import home_screen, load_featured_products

app_name = 'main'

urlpatterns = [
    path('', home_screen, name='home-screen'),
    path('load_featured_products', load_featured_products, name='load-featured-products'),
]