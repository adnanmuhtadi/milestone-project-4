from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    # to assign the request as an attribute of the class, so we can access any attribute of the request coming from stripe
    def __init__(self, request):
        self.request = request

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
