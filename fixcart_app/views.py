from django.shortcuts import render


def home(request):
    return render(request, 'fixcart_app/index.html')

def about(request):
    return render(request, 'fixcart_app/about.html')

def contact(request):
    return render(request, 'fixcart_app/contact.html')
