from django.forms import ModelForm
from product.models import Product


class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price',  'status',  'image']

    # def save(self, commit=True):
    #     product = super().save(commit)
    #
    #     return product


class ProductEditForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price',  'status',  'image')
