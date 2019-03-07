from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title        = forms.CharField(max_length=30, help_text='30 characters max.',widget=forms.TextInput(attrs={'placeholder':'Enter title'}))
    product_type = forms.CharField(max_length=10, help_text='10 characters max.')
    price        = forms.DecimalField(label='Product price',initial=100)

    class Meta:
        model = Product
        fields = ['title','product_type','price']

    # validation methods
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')

        if title[0].islower():
            raise forms.ValidationError('Title must start with uppercase')
        return title


class RawProductForm(forms.Form):
    title        = forms.CharField(max_length=30, help_text='30 characters max.',widget=forms.TextInput(attrs={'placeholder':'Enter title'}))
    product_type = forms.CharField(max_length=10, help_text='10 characters max.')
    price        = forms.DecimalField(label='Product price',initial=100)

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')

        if title[0].islower():
            raise forms.ValidationError('Title must start with uppercase')
        return title


