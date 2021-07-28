import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile

# Will handle all orders across the store


class Order(models.Model):
    # Editable field means the field can not be changed was created
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    address_line1 = models.CharField(max_length=80, null=False, blank=False)
    address_line2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county_state = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(
        blank_label='Country *', null=False, blank=False)
    # Auto_now will be automatically generated as soon as the
    # user presses the buy now button
    purchase_date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """"
        The underscore is to define that it is a private method
        which would only be used inside this class but this class is to create
        a random and unique order number using the UUID
        """
        return uuid.uuid4().hex.upper()

        print(self.order_number)

    def update_final_total(self):
        """
        Update the final total each time a line item has been added
        and the delivery costs
        """
        # Setting the order total to lineitem_total_sum, by adding
        # 0 at the end, it will prevent an error if we manually delete all the
        # line items for an order by making sure that this sets the
        # order total to 0
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        # Using what has been set in settings for delivery cost and
        # standard delivery percentage
        if self.order_total < settings.FREE_DELIVERY_LIMIT:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_price = self.order_total + self.delivery_cost
        self.save()


    def save(self, *args, **kwargs):
        """
        Will override the original save method to set the order number,
        If it has not already been set.
        """
        # If the order does not have an order number, it will
        # create one and then save
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    # String method to return the order number
    def __str__(self):
        return self.order_number

    """
    Order Line Product class is set up so when an order instance is created,
    it will go through the list of line items, amend the calculations if
    need to be, and then attach it to the order.
    """


class OrderLineItem(models.Model):
    # The related name is so we can the call easier to make,
    # for example order.lineitems.filter
    order = models.ForeignKey(
        Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True)
    product_sold = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the line item total
        update the order total
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    # String method to return the sku of each product along with the
    # order number for which it is related to
    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
