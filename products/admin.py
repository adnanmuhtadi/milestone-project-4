from django.contrib import admin
from .models import Product, Category


# Displaying a list for the product details in the admin page
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'colour',
        'size',
        'has_sold',
        'image',
        'image_two',
        'image_three',
        'image_four',
    )

# Ordering the products by the sku name
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'readable_name',
        'name',
    )


# Registering the classes to the product and category models.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
