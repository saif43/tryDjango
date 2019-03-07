from django import forms

from .models import Person

class PersonForm(forms.ModelForm):
    name        = forms.CharField(label='Name',max_length=200)
    birthdate   = forms.DateField(label='Birthdate',widget=forms.TextInput(attrs={'placeholder':'yyyy-mm-dd'}))
    fathername  = forms.CharField(label="Father's name",max_length=200)
    mothername  = forms.CharField(label="Mother's name",max_length=200)
    school      = forms.BooleanField(label='School')
    college     = forms.BooleanField(label='Collage')
    university  = forms.BooleanField(label='University')

    class Meta:
        model = Person
        fields = ['name','birthdate','fathername','mothername','school','college','university']

    