from django.shortcuts import render


def home(request):
    return render(request, 'shop/shop.html', {'title': 'Shop'})
