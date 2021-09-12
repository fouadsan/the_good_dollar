from django.http.response import JsonResponse
from django.core.mail import send_mail
from django.core.mail import BadHeaderError
from django.shortcuts import redirect, render

from .forms import ContactMe


def contact(request):
    form = ContactMe(request.POST or None)
    return render(request, 'contact/contact.html', {'form': form})


def send_email(request):
    if request.is_ajax():
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        core = f"{message}.\nfrom: {name}, {email}"

        if name and email and subject and message:
            try:
                send_mail(subject, core, email,
                          ['f.benayad95@gmail.com'])
            except BadHeaderError:
                return JsonResponse({
                    'msg': 'Invalid header found.',
                    'type': 'error',
                    'confirmation': 'true',
                })
            return JsonResponse({
                'msg': 'Your email has been sent successfully to Fouad',
                'type': 'success',
                'confirmation': 'true'
            })
        else:
            return JsonResponse({
                'msg': 'Make sure all fields are entered are valid.',
                'type': 'error',
                'confirmation': 'true'
            })
    return redirect('contact:contact')
