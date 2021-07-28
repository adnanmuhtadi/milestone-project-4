from django.db import models

# Category model while it is being inherted from models.Model


class Category(models.Model):

    # To fix the name in the admin page
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    # Field being optional
    readable_name = models.CharField(max_length=254, null=True, blank=True)

    # String which returns the name of the category
    def __str__(self):
        return self.name

    # String to return the readable name
    def get_friendly_name(self):
        return self.readable_name


# Product model


class Product(models.Model):
    # Foreign key to the category modal, it also being an option field
    # if category is deleted, will give all products a null for this field
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    colour = models.CharField(max_length=254, null=True, blank=False)
    has_sizes = models.BooleanField(default=True, null=True, blank=True)
    has_sold = models.BooleanField(default=False, null=True, blank=True)
    size = models.DecimalField(
        max_digits=6, decimal_places=0, null=True, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    imagetwo_url = models.URLField(max_length=1024, null=True, blank=True)
    imagetwo = models.ImageField(null=True, blank=True)
    imagethree_url = models.URLField(max_length=1024, null=True, blank=True)
    imagethree = models.ImageField(null=True, blank=True)
    imagefour_url = models.URLField(max_length=1024, null=True, blank=True)
    imagefour = models.ImageField(null=True, blank=True)

    # String to return the product name
    def __str__(self):
        return self.name
