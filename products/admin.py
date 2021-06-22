from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'size',
        'image',
    )

# ordering the products by the sku name
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'readable_name',
        'name',

    )


# Registering the classes to the product and category models.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
