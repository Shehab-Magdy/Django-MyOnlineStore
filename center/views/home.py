from django.shortcuts import render, redirect, get_object_or_404 
from center.models import Category, Product
from django.core.paginator import Paginator


def Index(request):
	if request.GET.get('catid'):
		cat_id = request.GET.get('catid')
	else:
		cat_id = -1

	categories = Category.objects.all()
	if cat_id == -1:
		prod = Product.objects.all()
		
	else:
		prod = Product.objects.filter(category_id = cat_id)
		
	paging = Paginator(prod,6)
	page = request.GET.get('page')
	products = paging.get_page(page)
	cat_name = int(cat_id)
	data = {'cats':categories, 'prods': products, 'catName':cat_name}
	return render(request,'home/index.html', data)


