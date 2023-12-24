import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from product.models import Product
from product.forms import ProductEditForm, ProductCreateForm


def check_product(pk, user):
	try:
		room = Product.objects.get(id=pk, user=user)
		return room
	except ObjectDoesNotExist:

		return False


class ProductView(View, LoginRequiredMixin):

	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('users:login')
		else:
			user = request.user
			products = Product.objects.filter(user=user)
			return render(request, 'product/list.html', {"products": products})


class AddProductView(View, LoginRequiredMixin):
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('users:login')
		else:
			create_product_form = ProductCreateForm()
			return render(request, 'product/add_product.html', {"create_product_form": create_product_form})

	def post(self, request):
		if not request.user.is_authenticated:
			return redirect('users:login')
		else:
			create_product_form = ProductCreateForm(
				data=request.POST,
				files=request.FILES
			)
			user = request.user
			if create_product_form.is_valid():
				instance = create_product_form.save(commit=False)
				instance.user = user
				instance.save()
				products = Product.objects.filter(user=user)
				return render(request, 'product/list.html', {"products": products})
			return render(request, 'product/add_product.html', {"create_product_form": create_product_form})


class ProductDetailView(View, LoginRequiredMixin):
	def get(self, request, product_id):
		if not request.user.is_authenticated:
			return redirect('users:login')
		else:
			user = request.user
			product = check_product(product_id, user)
			if not product:
				contex = {
					'error': "Bunday mahsulot topilmadi"
				}
				return render(request, "product/list.html", contex)
			return render(request, 'product/detail.html', {"product": product})


class ProductEditView(View, LoginRequiredMixin):
	def get(self, request, product_id):
		if not request.user.is_authenticated:
			return redirect('users:login')
		else:
			user = request.user
			product = check_product(product_id, user)
			if not product:
				contex = {
					'error': "Bunday mahsulot topilmadi"
				}
				return render(request, "product/list.html", contex)
			product_edit_form = ProductEditForm(instance=product)
			return render(
				request,
				"product/edit_product.html",
				{
					"product": product, "product_form": product_edit_form
				}
			)

	def post(self, request, product_id):
		if not request.user.is_authenticated:
			return redirect('users:login')
		else:
			user = request.user
			product = check_product(product_id, user)
			if not product:
				contex = {
					'error': "Bunday mahsulot topilmadi"
				}
				return render(request, "product/list.html", contex)
			product_edit_form = ProductEditForm(instance=product, data=request.POST, files=request.FILES)
			user = request.user
			if product_edit_form.is_valid():
				instance = product_edit_form.save(commit=False)
				instance.create_time = product.create_time
				instance.update_time = datetime.datetime.now()
				instance.user = user
				instance.save()
				return redirect(reverse("product:detail", kwargs={"product_id": product_id}))

			return render(request, "books/edit_review.html", {"product": product, "product_edit_form": product_edit_form})


class ConfirmDeleteProductView(LoginRequiredMixin, View):
	def get(self, request, product_id):
		if not request.user.is_authenticated:
			return redirect('users:login')
		else:
			user = request.user
			product = check_product(product_id, user)
			if not product:
				contex = {
					'error': "Bunday mahsulot topilmadi"
				}
				return render(request, "product/list.html", contex)

			return render(request, "product/confirm_delete_product.html", {"product": product})


class DeleteProductView(LoginRequiredMixin, View):
	def get(self, request, product_id):
		if not request.user.is_authenticated:
			return redirect('users:login')
		else:
			user = request.user
			product = check_product(product_id, user)
			if not product:
				contex = {
					'error': "Bunday mahsulot topilmadi"
				}
				return render(request, "product/list.html", contex)
			product.delete()
			messages.success(request, "You have successfully deleted this review")

			return redirect(reverse("product:product"))
