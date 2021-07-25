from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_basket(request):
    """ 
    A view that loads the basket contents page 
    """

    return render(request, 'basket/basket.html')


# Function to take both the request and add the product id to the basket
def add_to_basket(request, item_id):
    """ 
    Add a quantity of the specified product to the shopping basket 
    """

    # Get the quantity from the the and url to redirect the user to
    product = get_object_or_404(Product, pk=item_id)
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # Session created till the browser is closed to keep the user 
    # shopping or if they would like to come back to it
    basket = request.session.get('basket', {})

    # If statement to check if a product with sizes is added or not.
    if size:
        # If the product is in basket
        if item_id in list(basket.keys()):
            # Condition: has the same size, increase quantity
            if size in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][size] = quantity
                messages.error(
                request, f'{product.name} is already in the basket')
            else:
                # Same item, different size, add it as a new item.
                basket[item_id]['items_by_size'][size] = quantity
        else:
            basket[item_id] = {'items_by_size': {size: quantity}}
    else:
        # Adding the product and quantity in the basket, and if the product is already there, add the quantity to the basket
        if item_id in list(basket.keys()):
            messages.error(
                request, f'{product.name} is already in the basket')
        else:
            basket[item_id] = quantity
            messages.success(request, f'{product.name} has been added to the basket.')

    # Overwriting the variable in the session with the updated version of the basket
    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)


# Function to remove the product from the basket
def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket"""

    # Try block to catch any expections that might happen with a server 500 error
    try:
        product = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})
        basket.pop(item_id)

        request.session['basket'] = basket
        messages.success(request, f'{product.name} has been removed from the basket.')
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item {e}')
        return HttpResponse(status=500)
