from django.shortcuts import render


def home_screen(request):
    return render(request, 'main/home_screen.html')
