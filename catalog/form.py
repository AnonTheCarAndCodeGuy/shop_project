from django import forms
from catalog.models import Car, Brand
from django.contrib.auth.models import User

'''
The purpose of this file is to be an interface between the model and the view.
Because in 3 layered architecture, front end and backend is separated.
'''

class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        widgets = {'owner': forms.HiddenInput}



class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','password','first_name','last_name')
        labels = {'username':'email'}
        widgets = {'password': forms.PasswordInput}
