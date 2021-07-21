from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    # Set of empty path to indicate this is the route URL, and its going to render views.checkout with the name checkout.

    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>',
         views.checkout_success, name='checkout_success'),
    path('wh/', webhook, name='webhook'),
]
