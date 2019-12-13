from center.models import Product, Category
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

def admin_index(request):
	prods = Product.objects.count()
	cats = Category.objects.count()
	return render(request, 'home/admin_index.html',{'prodcount':prods, 'catcount':cats})
