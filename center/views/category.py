from django.shortcuts import render, redirect, get_object_or_404
from center.models import Category, product
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.db.models import Count

def index(request):
	cats = Category.objects.all()
	catcount = Category.objects.annotate(prods=Count('product'))
	return render(request, 'category/category.html', {'categories': catcount, 'prodscount':catcount})

def show(request,cat_id):
	try:
		#cat = Category.objects.get(pk=cat_id)
		cat = get_object_or_404(Category, pk=cat_id)
		return render(request,'category/category_details.html',{'category':cat})
	except DoesNotExist:
		return HttpResponse("item not found")

def delete(request,cat_id):
	cat = Category.objects.get(pk=cat_id)
	cat.delete()
	return redirect(reverse('center:Category_List'))

def create(request):
	if request.method == 'GET':
		return render(request,'category/category_update.html')
	elif request.method == 'POST':
#def save(request):
		name = request.POST.get('cat_name')
		description = request.POST.get('cat_desc')
		newCat = Category()
		newCat.name = name
		newCat.description = description
		newCat.save()
		#Category.objects.create(name = name, description = description)
		return redirect(reverse('center:Category_List'))

def update(request, cat_id):
	if request.method == 'GET':
		#cat = Category.objects.get(pk=cat_id)
		cat = get_object_or_404(Category, pk=cat_id)
		return render(request,'category/category_update.html',{'category':cat})
	elif request.method == 'POST':
#def saveupdate(request, cat_id):
		var_name = request.POST.get('cat_name')
		var_description = request.POST.get('cat_desc')
		Category.objects.filter(pk=cat_id).update(name = var_name, description = var_description)
		return redirect(reverse('center:Category_List'))
		
