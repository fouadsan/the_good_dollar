from django.shortcuts import render


def home_screen(request):
    return render(request, home_screen)


def profile_screen(request):
    return render(request, home_screen)

def signup_screen(request):
    return render(request, home_screen)
