from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm


# Create your views here.


def all_products(request):
    """ A view to show all the products, including the sorting and searching,
    Context is added to send things back to the template"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    # checking if category request.GET exists
    if request.GET:
        if 'sort' in request.GET:
            # allowing sort to also equals sortkey
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                # rename sortkey to lower_name in the event user sorting by name
                sortkey == 'lower_name'
                # annotate the list of products with the new field
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                # check if the direction is descending or ascending
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            # to sort the products
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            # take the list of results and split in the ','
            categories = request.GET['category'].split(',')
            # using that list, it will filter the products based on the name of the categories
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # checking if request.GET exists and using the search_q parameters
        # if search_q is in request.GET then call it query
        if 'search_q' in request.GET:
            query = request.GET['search_q']
            # Error message appear if query is blank, and then redirects them to products view
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            # setting a variable to Q object where it is searching content using the name or description
            search_results = Q(name__icontains=query) | Q(
                description__icontains=query)
            # pass the results through the filter method
            products = products.filter(search_results)

    sorting_products = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'present_categories': categories,
        'sorting_products': sorting_products,
    }

    return render(request, 'products/products.html', context)

# Product detail view


def product_detail(request, product_id):
    """ 
    A view to show a specific product by take the parameter Product ID, 
    Context is added to send things back to the template
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ 
    Add a product to the store, it will render an empty instance of our form,
    a new template, and will include context which includes the product form
    """
    # to ensure we capture the image, then we are checking if the form is valid
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def edit_product(request, product_id):
    """
    Edit a product in store
    """
    # prefilling the form using the product_objetc_or_404
    product = get_object_or_404(Product, pk=product_id)
    # checking if the request method is post, telling the instance to post new information of that instance of the product.
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid')
    else:
    # creating the1 instance of the product form
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    # informing it which template to use.
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)