from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):
    # empty list for the bag items to live in which will return a dictionary

    basket_products = []
    total = 0
    item_count = 0
    # adding the basket so it works throughout the site
    basket = request.session.get('basket', {})

    # for each item and quantity within the basket, get the product then the basket and its calculations
    for item_id, item_data in basket.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            item_count += item_data
            # add a dictionary to the list of basket items containing the Item, quantity and product
            basket_products.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                # add a dictionary to the list of basket items containing the Item, quantity and product
                basket_products.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                }) 

    # they will receive free delivery if they spend more than the amount specified in the settings.py
    if total < settings.FREE_DELIVERY_LIMIT:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_message = settings.FREE_DELIVERY_LIMIT - total
    else:
        # delivery will be 0 if they meet the delivery limit
        delivery = 0
        free_delivery_message = 0

    # calculations to add the delivery to the grand total
    grand_price = delivery + total

    # adding items to the context which will available to all templates across the site
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
