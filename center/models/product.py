from django.db import models
from .category import Category


class Product(models.Model):
	"""docstring for ClassName: creating table Products"""
	name = models.CharField(max_length=100)
	price = models.FloatField()
	description = models.TextField()
	photo = models.ImageField(upload_to='media/center/product/' ,null=True)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)

	def __str__(self):
		return self.name