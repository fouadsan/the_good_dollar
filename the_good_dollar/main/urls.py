from django.urls import path

from .views import home_screen

app_name = 'main'

urlpatterns = [
    path('', home_screen, name='home-screen'),
]