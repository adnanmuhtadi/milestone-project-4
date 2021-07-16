from django.contrib import admin
from .models import Order, OrderLineProduct
# Register your models here.


class OrderLineProductAdminInline(admin.TabularInline):
    # admin class enabling you to add and edit line products in admin page
    model = OrderLineProduct
    readonly_fields = ('lineproduct_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineProductAdminInline,)

    # fields that can not be edited, would be calculated bu the model method,
    readonly_fields = ('profile', 'order_number', 'purchase_date',
                       'delivery_cost', 'order_total',
                       'grand_price',)

    # specify the order which is should be displayed in the admin interface
    fields = ('order_number', 'profile', 'full_name', 'email', 'phone_number',
              'address_line1', 'address_line2', 'town_or_city', 'county_state',
              'postcode', 'country', 'purchase_date', 'delivery_cost', 'order_total',
              'grand_price',)

    # To restrict the column that show up in the order list
    list_display = ('order_number', 'purchase_date', 'full_name',
                    'order_total', 'delivery_cost', 'grand_price',)

    # Ordering the display column to newest first (date)
    ordering = ('-purchase_date',)


admin.site.register(Order, OrderAdmin)
