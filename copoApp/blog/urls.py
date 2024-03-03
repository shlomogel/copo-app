from django.urls import path
from .views import (
    HomeView,
    ProductDetailView,
    ProductCreateView,
    logout_user,
    login_user,
    about,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("product/<int:pk>", ProductDetailView.as_view(), name="product-detail"),
    path("add/", ProductCreateView.as_view(), name="add_product"),
    path("about/", about, name="about"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]
