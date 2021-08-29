from django.shortcuts import render
from django.shortcuts import render


def home_screen(request):
    return render(request, 'blog/home_screen.html')

def detail_screen(request, _id):
    return render(request, 'blog/detail_screen.html')
