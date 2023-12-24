
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api.views import ProductApiView, ProductDetailApiView
app_name = "api"
urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', ProductApiView.as_view(), name='product'),
    path('<int:product_id>', ProductDetailApiView.as_view(), name='detail'),
]



