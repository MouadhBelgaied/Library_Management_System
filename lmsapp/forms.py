from django import forms
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields= [
            'title' ,
            'author' ,
            'photo_book', 
            'photo_author', 
            'pages' ,
            'price' ,
            'rental_price_day', 
            'rental_period' ,
            'total_rental',
            'active' ,
            'state' ,
            'Category', 
        ]
        widgets= {  
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control'}),
            'photo_book' : forms.FileInput(attrs={'class':'form-control'}),
            'photo_author' : forms.FileInput(attrs={'class':'form-control'}),
            'pages' : forms.NumberInput(attrs={'class':'form-control'}),
            'price' : forms.NumberInput(attrs={'class':'form-control'}),
            'rental_price_day' : forms.NumberInput(attrs={'class':'form-control','id':'rental_price_day'}),
            'rental_period' : forms.NumberInput(attrs={'class':'form-control','id':'rental_period'}),
            'total_rental' : forms.NumberInput(attrs={'class':'form-control','id':'total_rental', 'readonly': 'readonly'}),
            'active' : forms.CheckboxInput(),
            'state' : forms.Select(attrs={'class':'form-control'}),
            'Category' : forms.Select(attrs={'class':'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields= ['name']
        widgets= {  
            'name' : forms.TextInput(attrs={'class':'form-control'}),
        }