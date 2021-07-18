from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from basket.contexts import basket_contents

import stripe


def checkout(request):
    # setting up stripe payment intent
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    """
    gets the basket from the session and checks if it is empty or not,
    if there is nothing in the basket, it will direct the user to the products page
    """
    # handler to post the user details, first the check if the method is post
    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'county_state': request.POST['county_state'],
            'country': request.POST['country'],
        }
        # creating an instance of the form
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            size = request.POST['product_size']
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
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

        order_form = OrderForm()

    # alert if the public key hasnt been set
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Has it been forgotten to be set in the local environment?')

    # instance of the order form which would empty
    # creating the template and the creating the context containing the order form

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    # retrieving the shopping basket
    save_info = request.session.get('save_info')
    # using the order number to get the order created which will be sent back to the template
    order = get_object_or_404(Order, order_number=order_number)
    # success message letting the user know the order number
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation email \
        will be sent to {order.email}.')

    # deleting the user shopping basket from the session
    if 'basket' in request.session:
        del request.session['basket']

    # set the template and the context
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    # render the template
    return render(request, template, context)
