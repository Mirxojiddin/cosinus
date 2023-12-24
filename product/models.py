from django.db import models

from users.models import CostumeUser


class ProductStatus(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.name}"


class Product(models.Model):
	user = models.ForeignKey(CostumeUser, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	image = models.ImageField(default="product-placeholder.png")
	price = models.IntegerField()
	create_time = models.DateTimeField(auto_now=True)
	update_time = models.DateTimeField(auto_now=True)
	status = models.ForeignKey(ProductStatus, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.user.first_name} {self.user.last_name} {self.name}"