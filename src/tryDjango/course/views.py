from django.shortcuts import render

# Create your views here.

from django.views import View

def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html',{})
