from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    # importing the signals module, so whenever and product is saved or deleted,
    # the update total modal method gets called and automatically updates order total.
    def ready(self):
        import checkout.signals
