from django.shortcuts import render, get_object_or_404, Http404, redirect
from .models import Product

from .forms import ProductForm, RawProductForm

# Create your views here.

def product_create_view(request):
    
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm() # doesn't show prev inputs

    contexts = {
        'form' : form
    }
    
    return render(request,'product/create.html',contexts)


def dynamic_lookup_view(request,p_id):
    # obj = Product.objects.get(id=p_id)
    
    # product not found handling with get_object_or_404
    obj = get_object_or_404(Product, id=p_id)


    # product not found handling with http404
    # obj = Product.objects.get(id=p_id)
    # try:
    #     obj = Product.objects.get(id=p_id)
    # except Product.DoesNotExist:
    #     raise Http404


    contexts = {
        'object' : obj
    }
    
    return render(request,'product/detail.html',contexts)
    

def delete_product_view(request, p_id):
    obj = get_object_or_404(Product, id=p_id)

    if request.method == 'POST':
        obj.delete()
        return redirect('../../')

    contexts = {
        'object' : obj
    }
    
    return render(request,'product/delete.html',contexts)
    

# def product_create_view(request):
    
#     form = RawProductForm()    
#     if request.method == 'POST':
#         form = RawProductForm(request.POST)
    
#     if form.is_valid():
#         # print(form.cleaned_data)
#         Product.objects.create(**form.cleaned_data)
#         form = RawProductForm()
#     else:
#         print(form.errors)

#     contexts = {
#         'form' : form
#     }
    
    
#     return render(request,'product/create.html',contexts)
    

def product_list_view(request,*args, **kwargs):
    
    querySet = Product.objects.all()

    contexts = {
        'object_list' : querySet
    }
    
    return render(request,'product/allproducts.html',contexts)
    

def product_detail_view(request,*args, **kwargs):
    
    obj = Product.objects.get(id=2)

    contexts = {
        'object' : obj
    }
    
    return render(request,'product/detail.html',contexts)
    