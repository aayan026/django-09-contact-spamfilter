from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render

from .forms import ContactForm


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact/home.html')


def contact_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            request.session['contact_name'] = form.cleaned_data['name']
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {
        'form': form,
    })


def contact_success_view(request: HttpRequest) -> HttpResponse:
    name = request.session.get('contact_name', '')
    return render(request, 'contact/contact_success.html', {'name': name})
