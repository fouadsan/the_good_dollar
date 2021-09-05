import calendar

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models.functions import ExtractMonth
from django.db.models import Count

from .forms import UserRegisterForm, ProfileForm
from .models import Profile, CartOrder, CartOrderItems, AddressBook
from shop.models import ProductReview


def dashboard_screen(request):
    return render(request, 'users/dashboard.html')

def get_orders(request):
    orders = CartOrder.objects.annotate(month=ExtractMonth('order_dt')).values('month').annotate(count=Count('id')).values('month','count')
    month_number = []
    total_orders = []
    
    for d in orders:
        month_number.append(calendar.month_name[d['month']])
        total_orders.append(d['count'])
    
    if request.is_ajax():
        data = {
            'month_number': month_number,
            'total_orders': total_orders
        }
        return JsonResponse({'data': data})

def orders_screen(request):
    return render(request, 'users/orders.html')

def reviews_screen(request):
    reviews = ProductReview.objects.filter(user=request.user).order_by('-id')
    return render(request, 'users/reviews.html', {'reviews': reviews})


def add_addressbook(request):
    if request.is_ajax():
        return JsonResponse({'msg': 'hello world'})
    return redirect('users:addressbook')


def signup_screen(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(
                request, f'Your account has been created! You can now customize your profile')
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('users:profile')
    else:
        form = UserRegisterForm()

    context = {
        'header': 'Create New Account',
        'form': form,
    }

    return render(request, 'users/signup.html', context)


@login_required
def profile_screen(request):
    obj = Profile.objects.get(user=request.user)
    form = ProfileForm(request.POST or None, instance=obj)
    if request.is_ajax():
        if form.is_valid():
            instance = form.save()
            return JsonResponse({
                'user': instance.user.username,
                'email': instance.email,
                'phone': instance.phone,
                'first_name': instance.first_name,
                'last_name': instance.last_name,
                'address': instance.address,
                'city': instance.city,
            })
    context = {
        'section_title': 'Users',
        'title': 'Profile',
        'obj': obj,
        'form': form,
    }

    return render(request, 'users/profile.html', context)


# Orders
def orders(request):
	orders = CartOrder.objects.filter(user=request.user).order_by('-id')
	return render(request, 'user/orders.html',{'orders': orders})

# Order Detail
def order_items(request,id):
	order = CartOrder.objects.get(pk=id)
	orderitems = CartOrderItems.objects.filter(order=order).order_by('-id')
	return render(request, 'user/order-items.html',{'orderitems': orderitems})


# AddressBook
def addressbook_screen(request):
    addrbook = AddressBook.objects.filter(user=request.user).order_by('-id')
    print(addrbook)
    return render(request, 'users/addressbook.html', {'addrbook': addrbook})