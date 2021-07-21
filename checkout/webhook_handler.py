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
            content=f'Webhook received: {event["type"]}',
            status=200)