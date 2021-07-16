from django.urls import path
from . import views

urlpatterns = [
    # Set of empty path to indicate this is the route URL, and its going to render views.checkout with the name checkout.

    path('', views.checkout, name='checkout')
]
