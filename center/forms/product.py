from django import forms
from center.models import Category
class ProductForm (forms.Form):
    name  = forms.CharField(label='name',max_length=40)
    price = forms.FloatField(help_text='Numeric value')
    description = forms.CharField(label='description',max_length=250)
    photo = forms.ImageField(label='photo')
    # category = forms.ForeignKey(Category, on_delete = forms.CASCADE)
    
    # InlineForeignKeyField()

