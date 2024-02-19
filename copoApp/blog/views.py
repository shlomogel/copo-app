from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Product
from .forms import ProductForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


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


class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "add_product.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        return self.request.user.is_superuser
