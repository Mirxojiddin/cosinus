from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

from api.serializers import ProductSerializer
from product.models import Product


def check_product(pk, user):
	try:
		room = Product.objects.get(id=pk, user=user)
		return room
	except ObjectDoesNotExist:

		return False


class ProductApiView(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	def get(self, request, *args, **kwargs):
		product = Product.objects.all()
		serializer = ProductSerializer(product, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request, *args, **kwargs):
		serializer = ProductSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailApiView(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self, request, product_id):
		user = request.user
		product = check_product(product_id, user)
		if not product:
			contex = {
				'error': "Bunday mahsulot topilmadi"
			}
			return Response(contex, status=status.HTTP_404_NOT_FOUND_OK)
		serializer = ProductSerializer(product)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, product_id):
		user = request.user
		product = check_product(product_id, user)
		if not product:
			contex = {
				'error': "Bunday mahsulot topilmadi"
			}
			return Response(contex, status=status.HTTP_404_NOT_FOUND_OK)
		serializer = ProductSerializer(product)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, product_id):
		user = request.user
		product = check_product(product_id, user)
		if not product:
			contex = {
				'error': "Bunday mahsulot topilmadi"
			}
			return Response(contex, status=status.HTTP_404_NOT_FOUND_OK)
		product.delete()
		return Response({"message": "o'chirildi"}, status=status.HTTP_204_NO_CONTENT)




class DeleteProductView(APIView):
	def delete(self, request, product_id):
		user = request.user
		product = check_product(product_id, user)
		if not product:
			contex = {
				'error': "Bunday mahsulot topilmadi"
			}
			return Response(contex, status=status.HTTP_404_NOT_FOUND_OK)
		product.delete()
		return Response({"message": "o'chirildi"}, status=status.HTTP_404_NOT_FOUND)
