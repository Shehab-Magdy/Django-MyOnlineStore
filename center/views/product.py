from center.models import Product, Category
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

def index(request):
	prods = Product.objects.select_related('category').all()
	return render(request, 'product/product.html', {'products': prods})

def show(request,prod_id):
	#try:
		#pro = Product.objects.select_related('category').get(pk=prod_id)
	pro = get_object_or_404(Product.objects.select_related('category'),pk=prod_id)
	return render(request,'product/product_details.html',{'product':pro})
	#except Exception as e:
	#	return HttpResponse("Item not found")

def delete(request,prod_id):
	prod = Product.objects.get(pk=prod_id)
	prod.delete()
	return redirect(reverse('center:Product_List'))

def create(request):
	if request.method == 'GET':
		categories = Category.objects.all()
		return render(request,'product/product_update.html',{'cats':categories})
	elif request.method == 'POST':
#def save(request):
		name = request.POST.get('prod_name')
		desc = request.POST.get('prod_desc')
		price =  request.POST.get('prod_price')
		prphoto = request.FILES['prod_photo']
		cat = request.POST.get('prod_cat')
		newProd = Product()
		newProd.name = name
		newProd.price = price
		newProd.description = desc
		newProd.photo = prphoto
		newProd.category = Category.objects.get(id=cat)
		newProd.save()
		#Product.objects.create(name = name,price = price, description = description, category = Category.objects.get(id=cat))
		return redirect(reverse('center:Product_List'))


def update(request, prod_id):
	if request.method == 'GET':
		prod = get_object_or_404(Product, pk=prod_id)
		cat = Category.objects.all()
		return render(request,'Product/product_update.html',{'prod':prod,'cats':cat})
	elif request.method == 'POST':
#def saveupdate(request, prod_id):
		prod = get_object_or_404(Product, pk=prod_id)
		prod.name = request.POST.get('prod_name')
		prod.description = request.POST.get('Prod_desc')
		prod.price = request.POST.get('prod_price')
		prod.photo = request.FILES['prod_photo']
		cat_id = request.POST.get('prod_cat')
		prod.category = Category.objects.get(id=cat_id)
		prod.save()
		return redirect(reverse('center:Product_List'))
		
