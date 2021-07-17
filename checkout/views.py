from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from basket.contexts import basket_contents

import stripe


def checkout(request):
    # setting up stripe payment intent
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    """
    gets the basket from the session and checks if it is empty or not,
    if there is nothing in the bag, it will direct the user to the products page
    """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(
            request, "There's nothing in the your basket at the moment")
        return redirect(reverse('products'))

    # setting up the secret key on stripe and payment intent giving it the amount and currency
    current_basket = basket_contents(request)
    total = current_basket['grand_price']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    # alert if the public key hasnt been set
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Has it been forgotten to be set in the local environment?')

    # instance of the order form which would empty
    # creating the template and the creating the context containing the order form
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
