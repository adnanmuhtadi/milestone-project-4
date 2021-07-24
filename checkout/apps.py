from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    # Importing the signals module, so whenever and product is saved or deleted,
    # the update total modal method gets called and automatically updates order total.
    def ready(self):
        import checkout.signals
