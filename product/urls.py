from django.urls import path
from product.views import ProductView, ProductDetailView, ProductEditView, ConfirmDeleteProductView, DeleteProductView,AddProductView

app_name = "product"
urlpatterns = [
	path('', ProductView.as_view(), name='product'),
	path('add', AddProductView.as_view(), name='add-product'),
	path('<int:product_id>', ProductDetailView.as_view(), name='detail'),
	path('<int:product_id>/edit', ProductEditView.as_view(), name='edit-product'),

	path(
		"<int:product_id>/delete/confirm/",
		ConfirmDeleteProductView.as_view(),
		name="confirm-delete-product"
	),
	path(
		"<int:product_id>/delete/",
		DeleteProductView.as_view(),
		name="delete-product"
	),

]
