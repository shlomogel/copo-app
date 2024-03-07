from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("register/", views.register_user, name="register"),
    path("product/<int:pk>", views.ProductDetailView.as_view(), name="product-detail"),
    path("add/", views.ProductCreateView.as_view(), name="add_product"),
    path("about/", views.about, name="about"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("product/<int:pk>/delete/", views.ProductDeleteView.as_view(), name="delete"),
]
