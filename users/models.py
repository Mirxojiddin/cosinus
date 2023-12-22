from django.contrib.auth.models import AbstractUser
from django.db import models


class CostumeUser(AbstractUser):
	avatar = models.ImageField(default="default_photo.jpg")
	phone_number = models.CharField(max_length=13)

	def __str__(self):
		return f"{self.username} {self.last_name}"
