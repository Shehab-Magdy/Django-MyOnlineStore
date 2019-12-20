from django.db import models
from .product import Product

class Like(models.Model):
	"""docstring for Like"""
		
	product = models.ForeignKey(Product, on_delete = models.CASCADE)

