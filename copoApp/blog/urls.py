from django.urls import path
from .views import HomeView, ProductDetailView, ProductCreateView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("product/<int:pk>", ProductDetailView.as_view(), name="product-detail"),
    path("add/", ProductCreateView.as_view(), name="add_product"),
]
