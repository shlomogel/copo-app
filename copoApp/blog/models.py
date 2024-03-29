from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    main_image = models.URLField()
    group_url = models.URLField()
    description = models.TextField()
    likes = models.IntegerField(default=0)
    saved_by = models.ManyToManyField(User, related_name="saved_posts")
    date_published = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(to=Tag, related_name="products", blank=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField(default=datetime.now() + timedelta(weeks=2))

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    img_url = models.URLField()

    def __str__(self):
        return f"Image for {self.product.title}"


class Comment(models.Model):
    product = models.ForeignKey(
        Product, related_name="comments", on_delete=models.CASCADE
    )
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.date} on {self.product.title}"
