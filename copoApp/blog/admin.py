from django.contrib import admin
from .models import Product, Tag, ProductImage

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Tag)
