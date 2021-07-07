from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):
    # Will return a dictionary

    basket_products = []
    total = 0
    item_count = 0
    # adding the basket so it works throughout the site
    basket = request.session.get('basket', {})

    # for each item and quantity within the basket, get the basket and then set the calculations
    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        item_count += quantity
        # add a dictionary to the list of basket items containing the Item, quantity and product
        basket_products.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    # they will receive free delivery if they spend more than the amount specified in the settings.py
    if total < settings.FREE_DELIVERY_LIMIT:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_message = settings.FREE_DELIVERY_LIMIT - total
    else:
        # delivery will be 0 if they meet the threshold
        delivery = 0
        free_delivery_message = 0

    # calculations of the grand total
    grand_price = delivery + total

    # adding items to the context
    context = {
        'basket_products': basket_products,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'free_delivery_message': free_delivery_message,
        'free_delivery_limit': settings.FREE_DELIVERY_LIMIT,
        'grand_price': grand_price,
    }

    return context
