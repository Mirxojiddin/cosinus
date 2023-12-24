from rest_framework import serializers
from users.models import CostumeUser
from product.models import Product, ProductStatus
from rest_framework.exceptions import ValidationError


class CostumeUserSerializer(serializers.ModelSerializer):
	first_name = serializers.CharField(max_length=100, required=True, error_messages={
		'required': "First_name  kiritilmagan"
	})
	last_name = serializers.CharField(max_length=100, required=True, error_messages={
		'required': "last_name  kiritilmagan"
	})
	avatar = serializers.ImageField(default="default_photo.jpg" )
	phone_number = serializers.CharField(max_length=17, required=True, error_messages={
					'max_length': "Telephone xato kiritilgan ",
					'required': "Telephone  kiritilmagan"
				})

	class Meta:
		model: CostumeUser
		fields = ('first_name', 'last_name', 'password', 'phone_number', 'avatar')

	def validate_phone_number(self, value):
		check_value = value.replace(' ', '')
		if len(check_value) != 13:
			raise ValidationError("Telephone ma'lumotlari xato kiritilgan")
		return check_value


class ProductSerializer(serializers.ModelSerializer):
	name = serializers.CharField(max_length=100, required=True, error_messages={
		'max_length': "Name ortiqcha kiritilgan",
		'required': "Name kiritilmagan"
	})
	price = serializers.IntegerField(min_value=1, error_messages={
			'required': "Price kiritilmagan",
			'min_value': "Eng kichik qiymat 1 bo'lishi kerak"
	})

	image = serializers.ImageField(default="product-placeholder.png", error_messages={
			'required': "Image kiritilmagan"
	})
	status = serializers.IntegerField(min_value=1, max_value=2, required=True, error_messages={
			'required': "status kiritilmagan",
			'min_value': "qiyamt 1 yoki 2 bo'lishi kerak",
			'max_value': "qiyamt 1 yoki 2 bo'lishi kerak"
	})
	user_id = serializers.IntegerField(write_only=True)
	user = CostumeUserSerializer(read_only=True)

	class Meta:
		model = Product
		fields = ['name', 'price', 'status', 'image', 'user_id', 'user']


