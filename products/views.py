from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to show all the products, including the sorting and searching,
    Context is added to send things back to the template"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
