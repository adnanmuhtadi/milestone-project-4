from django.shortcuts import get_object_or_404, render, redirect, reverse, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from basket.contexts import basket_contents

import stripe
import json


# Checking that the user has selected the save info box on checkout
@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        # Stepping up stripe with the secret ID
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # Modifying the metadata
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        # Returning a HTTPResponse responding if the status is ok
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Your payment cannot currently be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    # Setting up stripe payment intent
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    """
    Gets the basket from the session and checks if it is empty or not,
    if there is nothing in the basket, it will direct
    the user to the products page
    """
    # Handler to post the user details, first the check if the method is post
    if request.method == 'POST':
        basket = request.session.get('basket', {})
        print(basket)

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
        # Creating an instance of the form
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()
            # Taken from my basket context.py and altered for the checkout app
            for item_id, item_data in basket.items():
                try:
                    # Getting product id, if product hasn't got sizes, then it
                    # will save the order_line_item
                    product = Product.objects.get(id=item_id)
                    # When product has been sold, it would change the
                    # status to true
                    product.has_sold = True
                    product.save()
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                            product_size=product.size,
                        )
                        order_line_item.save()
                    else:
                        # If the product id has got sizes, then it will
                        # print the following line items.
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't \
                            found in our database."
                        "Please contact us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information and try again.')
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(
                request, "The basket is currently empty")
            return redirect(reverse('products'))

        # Setting up the secret key on stripe and payment
        # intent giving it the amount and currency
        current_basket = basket_contents(request)
        total = current_basket['grand_price']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # If the user is authenticated, their profile information
        # would be retrieved. and have the input fields prefilled.
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'address_line1': profile.default_address_line1,
                    'address_line2': profile.default_address_line2,
                    'town_or_city': profile.default_town_or_city,
                    'county_state': profile.default_county_state,
                    'postcode': profile.default_postcode,
                    'country': profile.default_country,
                })

                # Empty form will be provided if the user is not authenticated.
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    # Alert if the public key hasnt been set
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Has it been forgotten to be set in the local environment?')

    # Instance of the order form which would empty creating the
    # template & the creating the context containing the order form

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
    # Retrieving the shopping basket
    save_info = request.session.get('save_info')
    # Using the order number to get the order created which
    # will be sent back to the template
    order = get_object_or_404(Order, order_number=order_number)

    # If statement to make sure the user is authenticated
    if request.user.is_authenticated:
        # Retrieving the user profile
        profile = UserProfile.objects.get(user=request.user)
        # Attaching the user's profile to the current order
        order.user_profile = profile
        order.save()

        # If the save info check box is checked, it will put
        # the info as it will match with the profile data model
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_address_line1': order.address_line1,
                'default_address_line2': order.address_line2,
                'default_town_or_city': order.town_or_city,
                'default_county_state': order.county_state,
                'default_postcode': order.postcode,
                'default_country': order.country,
            }

            # Using the profile data, an instance will be created,
            # and if the user form is valid, update user preferences.
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

            # Success message letting the user know the order number
            messages.success(request, f'Your order has been successfully processed! \
                Your order number is {order_number}. A confirmation email \
                will be sent to "{order.email}"')

    # Deleting the user shopping basket from the session
    if 'basket' in request.session:
        del request.session['basket']

    # Set the template and the context
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    # Render the template
    return render(request, template, context)
