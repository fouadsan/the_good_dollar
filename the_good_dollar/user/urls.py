from django.urls import path

from .views import dashboard_screen, get_orders, orders, order_items, reviews_screen, addressbook_screen, activate_address, get_addr_data, delete_address,\
     update_address, profile_screen

app_name = 'user'

urlpatterns = [
    path('dashboard/', dashboard_screen, name='dashboard'),
    path('orders_data',get_orders, name='get-orders-data'),
    path('profile', profile_screen, name='profile'),
    path('orders', orders, name='orders'),
    path('orders_items/<int:id>', order_items, name='order-items'),
    path('reviews', reviews_screen, name='reviews'),
    path('addressbook', addressbook_screen, name='addressbook'),
    path('activate_address/', activate_address, name='activate-address'),
    path('addr_data/<pk>', get_addr_data, name='address-data'),
    path('delete_addr/<pk>', delete_address, name='delete-address'),
    path('update_address/<pk>', update_address, name='update-address'),
]