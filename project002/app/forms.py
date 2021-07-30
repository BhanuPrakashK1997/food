
from django import forms
from .models import Recipes
#
# class ReciepesForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     ingredients = forms.CharField(max_length=200)
#     process = forms.CharField(max_length=100,initial='bhanu')
#     image = forms.ImageField()

class ReciepesForm(forms.ModelForm):
    class Meta:
        model=Recipes
        fields = '__all__'