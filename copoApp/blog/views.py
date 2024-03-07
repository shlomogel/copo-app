from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from .models import Product, ProductImage
from .forms import ProductForm, SignUpForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


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


class ProductDeleteView(SuccessMessageMixin, DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("home")

    def get_success_message(self, cleaned_data):
        return f"Product '{self.kwargs}' deleted successfully."


class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "add_product.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        form.instance.user = self.request.user
        # Save the main product first
        response = super().form_valid(form)
        # Then handle additional images
        additional_images = self.request.POST.get("images", "").split(",")
        for img_url in additional_images:
            ProductImage.objects.create(product=form.instance, img_url=img_url.strip())
        return response


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.success(request, (f"There was an error"))
            return redirect("login")
    else:
        return render(request, "login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logout..."))
    return redirect("home")


def about(request):
    return render(request, "about.html")


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You been registered"))
            return redirect("home")
        else:
            messages.success(request, (f"Ops "))
            return redirect("register")

    return render(request, "register.html", {"form": form})
