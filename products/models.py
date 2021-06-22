from django.db import models

# Category model while it is being inherted from models.Model


class Category(models.Model):
    name = models.CharField(max_length=254)
    # field being optional
    readable_name = models.CharField(max_length=254, null=True, blank=True)

    # string which returns the name of the category
    def __str__(self):
        return self.name

    # string to return the readable name
    def get_friendly_name(self):
        return self.readable_name
# Product model


class Product(models.Model):
    # foreign key to the category modal, it also being an option field
    # if category is deleted, will give all products a null for this field
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # string to return the product name
    def __str__(self):
        return self.name
