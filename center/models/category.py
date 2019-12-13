from django.db import models

class Category(models.Model):
	"""docstring for Category: creating table category"""
	name = models.CharField(max_length=50)
	description = models.TextField(null = True)

	def __str__(self):
		return self.name