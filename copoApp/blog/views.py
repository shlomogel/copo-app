from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


class HomeView(ListView):
    model = Product
    template_name = "home.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        comments = product.comments.all()  # Fetch comments associated with the product
        context["comments"] = comments
        return context
