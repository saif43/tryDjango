from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def view(request,*args, **kwargs):
#     return render(request, html_file, dictionary)

def home_view(request,*args, **kwargs):
    # return HttpResponse('<h1>Hello Worl d</h1>')
    return render(request,'home.html',{})

def contact_view(request,*args, **kwargs):
    # return HttpResponse('<h1>Contact page</h1>')
    return render(request,'contact.html',{})

def about_view(request,*args, **kwargs):
    # return HttpResponse('<h1>About page</h1>')
    my_context = {
        'my_name': 'SAIF AHMED ANIK',
        'my_number': '01674339903',
        'my_list': ['C','Java','C#','Python'],
    }
    return render(request,'about.html',my_context)

