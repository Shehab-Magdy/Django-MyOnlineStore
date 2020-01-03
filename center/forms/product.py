from django import forms

class ProductForm (forms.form):
    name  = forms.CharField(label='name',max_length=40)
	price = forms.FloatField()
    description = forms.CharField(label='description',max_length=250)
	photo = forms.ImageField(label='photo')
	category = forms.InlineForeignKeyField()
    ForeignKey(Category, on_delete = forms.CASCADE)

