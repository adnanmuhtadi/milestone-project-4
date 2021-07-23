from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    # to assign the request as an attribute of the class, so we can access any attribute of the request coming from stripe
    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Sends an email confirmation to the user
        """
        customer_email = order.email
        # render_to_string method takes the two files and puts them in a string 
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            # adding it to the context
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        # mail function to send the email
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )        

    def handle_event(self, event):
        """
        Takes the event stripe is sending us and returns a https response confirming it has been recieved
        """
        return HttpResponse(
            content=f'Unmanaged by Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handles the payment intent succeeded webhook from Stripe as this would be sent each time a 
        user makes a payment
        """
        intent = event.data.object
        print(intent)
        # getting the payment intent id, the basket, and the uses Save Info from the metadata 
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        # Storing the billing details/shipping details & Grand Price
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_price = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details to ensure the data is in the same form
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Handling the different checkout views for the user profiles for when the checkout view fails
        profile = None
        # Getting the username from intent.metadata, and so the user would be consider as not AnonymousUser
        username = intent.metadata.username
        if username != 'AnonymousUser':
            if save_info:
                # Getting user details as they are not anonymouse 
                profile = UserProfile.objects.get(user__username=username)
                profile.default_phone_number = shipping_details.phone
                profile.default_address_line1 = shipping_details.address.line1
                profile.default_town_or_city = shipping_details.address.city
                profile.default_address_line2 = shipping_details.address.line2
                profile.default_county_state = shipping_details.address.state
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_country = shipping_details.address.country
                profile.save()

        # checking if the order already exists and making and adding a delay
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    address_line1__iexact=shipping_details.address.line1,
                    town_or_city__iexact=shipping_details.address.city,
                    address_line2__iexact=shipping_details.address.line2,
                    county_state__iexact=shipping_details.address.state,
                    postcode__iexact=shipping_details.address.postal_code,
                    country__iexact=shipping_details.address.country,
                    grand_price=grand_price,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                # if the order has been found, the variable name 'order_exists' would be set to true and it would break out of the loop
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        # 200 response if the order has been found
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | Success!: The order has already been verified from our database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    address_line1=shipping_details.address.line1,
                    address_line2=shipping_details.address.line2,
                    county_state=shipping_details.address.state,
                    original_basket=basket,
                    stripe_pid=pid,
                )

            # Taken from my basket context.py and altered for the checkout app,
            # However, the data is being load from the JSON Version in the payment intent instead off from the session
                for item_id, item_data in json.loads(basket).items():
                    # Getting product id, if product hasn't got sizes, then it will save the order_line_item
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                            product_size=product.size
                        )
                        order_line_item.save()
                    else:
                        # If the product id has got sizes, then it will print the following line items.
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook handled received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Same as the payment intent succeeded, but handles it when it fails
        """
        return HttpResponse(
            content=f'Webhook handled received: {event["type"]}',
            status=200)
