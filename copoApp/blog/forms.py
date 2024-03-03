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
        widgets = {
            "title": forms.TextInput(attrs={"calss": "form-control"}),
            "img_url": forms.TextInput(attrs={"calss": "form-control"}),
            "group_url": forms.TextInput(
                attrs={"calss": "form-control", "placeholder": "Telegram Link"}
            ),
            "description": forms.Textarea(attrs={"calss": "form-control"}),
            "original_price": forms.NumberInput(attrs={"calss": "form-control"}),
            "discount_price": forms.NumberInput(attrs={"calss": "form-control"}),
        }
