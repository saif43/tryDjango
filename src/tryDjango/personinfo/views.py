from django.shortcuts import render, get_object_or_404
from .forms import PersonForm
from .models import Person

# Create your views here.

def person_create_view(request):
    
    form = PersonForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = PersonForm()

    contexts = {
        'form' : form
    }

    return render(request,'person/create.html',contexts)

def person_list_view(request,*args, **kwargs):

    querySet = Person.objects.all()

    context = {
        'personlist': querySet
    }

    return render(request,'person/view.html',context)

def dynamic_lookup_view(request,id):

    obj = get_object_or_404(Person, id=id)

    contexts = {
        'person' : obj
    }
    
    return render(request,'person/detail.html',contexts)