from django.contrib import admin
from .models import Order, OrderLineItem
# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    # admin class enabling you to add and edit line products in admin page
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    # fields that can not be edited, would be calculated bu the model method,
    readonly_fields = ('order_number', 'purchase_date',
                       'delivery_cost', 'order_total',
                       'grand_price', 'original_basket', 'stripe_pid')

    # specify the order which is should be displayed in the admin interface
    fields = ('order_number', 'user_profile', 'full_name', 'email', 'phone_number',
              'address_line1', 'address_line2', 'town_or_city', 'county_state',
              'postcode', 'country', 'purchase_date', 'delivery_cost', 'order_total',
              'grand_price', 'original_basket', 'stripe_pid')

    # To restrict the column that show up in the order list
    list_display = ('order_number', 'purchase_date', 'full_name',
                    'order_total', 'delivery_cost', 'grand_price',)

    # Ordering the display column to newest first (date)
    ordering = ('-purchase_date',)


admin.site.register(Order, OrderAdmin)
