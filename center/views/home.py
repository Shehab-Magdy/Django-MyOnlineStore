from django.shortcuts import render, redirect, get_object_or_404 
from center.models import Category, Product
from django.core.paginator import Paginator
from django.db.models import Q


def Index(request):
	categories = Category.objects.all()

	if request.GET.get('catid'):
		cat_id = request.GET.get('catid')
		cat_id = int(cat_id[0])
		if cat_id != 0:
			if request.GET.get('lt'):
				lt = int(request.GET.get('lt'))
				gt = int(request.GET.get('gt'))
				prod = Product.objects.filter(Q(price__lt=lt) & Q(price__gte=gt) &Q(category_id = cat_id))
			else:
				prod = Product.objects.filter(category_id = cat_id)
		else:
			if request.GET.get('lt'):
				lt = int(request.GET.get('lt'))
				gt = int(request.GET.get('gt'))
				prod = Product.objects.filter(Q(price__lt=lt) & Q(price__gte=gt))
	else:
		cat_id = 0
		prod = Product.objects.all()

	paging = Paginator(prod,6)
	page = request.GET.get('page')
	products = paging.get_page(page)
	cat_id = int(cat_id)
	data = {'cats':categories, 'prods': products, 'catNo':cat_id}
	return render(request,'home/index.html', data)


