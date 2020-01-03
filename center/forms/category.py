from django import forms

class CategoryForm (forms.form):
    name  = forms.CharField(label='name',max_length=40)
    description = forms.CharField(label='description',max_length=250)

    


