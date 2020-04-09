from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def about_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Hello world</h1>') # string of HTML code
     # The second parameter of render is the template, registered inside TEMPLATES array on project settings.py
    return render(request, 'about.html', {})


def contact_view(request, *args, **kwargs):
     # The second parameter of render is the template, registered inside TEMPLATES array on project settings.py
    return render(request, 'contact.html', {})


def home_view(request, *args, **kwargs):
     # The second parameter of render is the template, registered inside TEMPLATES array on project settings.py
    return render(request, 'home.html', {})

