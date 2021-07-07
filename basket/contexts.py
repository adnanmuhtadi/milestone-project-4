from decimal import Decimal
from django.conf import settings


def basket_contents(request):
    # Will return a dictionary

    basket_produts = []
    total = 0
    item_count = 0

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
        'basket_produts': basket_produts,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'free_delivery_message': free_delivery_message,
        'free_delivery_limit': settings.FREE_DELIVERY_LIMIT,
        'grand_price': grand_price,
    }

    return context
