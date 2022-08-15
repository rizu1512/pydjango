


from cProfile import label
from pyexpat import model
from attr import field
from django import forms
from .models import RedCat

class MyForm(forms.ModelForm):
    class Meta:
        model = RedCat
        fields = ["name","age",]
        labels = {'name': "name" , "age" : "age",}
        
