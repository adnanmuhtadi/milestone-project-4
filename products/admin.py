from django.contrib import admin
from .models import Product, Category

# Registering the product and category models.
admin.site.register(Product)
admin.site.register(Category)
