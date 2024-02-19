from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "img_url",
            "group_url",
            "description",
            "original_price",
            "discount_price",
        ]
