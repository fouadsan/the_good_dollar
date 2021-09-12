from django.urls import path

from .views import contact, send_email

app_name = 'contact'

urlpatterns = [
    path('', contact, name='contact'),
    path('send_email', send_email, name='send-email'),
]
