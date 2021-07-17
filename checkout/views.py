from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from basket.contexts import basket_contents
import environ

import stripe

env = environ.Env()
# reading .env file
environ.Env.read_env()


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

    current_basket = basket_contents(request)
    total = current_basket['grand_price']
    stripe_total = round(total * 100)

    # instance of the order form which would empty
    # creating the template and the creating the context containing the order form
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': env('STRIPE_PUBLIC_KEY'),
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
