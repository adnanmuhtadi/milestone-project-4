from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """
    gets the basket from the session and checks if it is empty or not,
    if there is nothing in the bag, it will direct the user to the products page
    """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(
            request, "There's nothing in the your basket at the moment")
        return redirect(reverse('products'))

    # instance of the order form which would empty
    # creating the template and the creating the context containing the order form
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
