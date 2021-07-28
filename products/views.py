from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """
    A view to show all the products, including the sorting and searching,
    Context is added to send things back to the template
    """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    # Checking if request.GET exists
    if request.GET:
        if 'sort' in request.GET:
            # Allowing sort to equals sortkey
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                # Rename sortkey to lower_name in the
                # Event user sorting by name
                sortkey == 'lower_name'
                # Annotate the list of products with the new field
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                # Check if the direction is descending or ascending
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            # To sort the products
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            # Take the list of results and split in the ','
            categories = request.GET['category'].split(',')
            # Using that list, it will filter the products
            # Based on the name of the categories
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Checking if request.GET exists and using the search_q parameters
        # If search_q is in request.GET then call it query
        if 'search_q' in request.GET:
            query = request.GET['search_q']
            # Error message appear if query is blank, and then
            # redirects them to products view
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            # Setting a variable to Q object where it is searching
            # Content using the name or description
            search_results = Q(name__icontains=query) | Q(
                description__icontains=query)
            # Pass the results through the filter method
            products = products.filter(search_results)

    sorting_products = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'present_categories': categories,
        'sorting_products': sorting_products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ 
    A view to show a specific product by take the parameter
    Product ID, context is added to send things back to the template
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


# @login required will make django check if the user is
# Already logged in or not. If not, it will redirect the user to the login page
@login_required
def add_product(request):
    """
    Add a product to the store, it will render an empty instance of our form,
    a new template, and will include context which includes the product form
    """
    # If not superuser, a message would be displayed and become
    # Redirected to the the home page
    if not request.user.is_superuser:
       messages.error(request, 'Sorry, only store owners can do that.')
       return redirect(reverse('home'))

    # To ensure we capture the image, then we are checking if the form is valid
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'{product.name} has been \
                successfully added!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add the product.\
            Please ensure the form is valid and try again.')
    else:
        form = ProductForm()
        
    # Adding context for the product admin
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in store
    """
    # If not superuser, a message would be displayed and become
    # Redirected to the the home page
    if not request.user.is_superuser:
       messages.error(request, 'Sorry, only store owners can do that.')
       return redirect(reverse('home'))

    # Prefilling the form using the product_object_or_404
    product = get_object_or_404(Product, pk=product_id)
    # Checking if the request method is post, telling the instance to
    # Post new information of that instance of the product.
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'{product.name} has now been \
                successfully updated!')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, f'Failed to update {product.name}. Please \
            ensure the form is valid and try again')
    else:
    # Creating the instance of the product form
        form = ProductForm(instance=product)
        messages.info(request, f'You are now editing {product.name}')

    # Informing it which template to use.
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from store
    """
    # If not superuser, a message would be displayed and become
    # Redirected to the the home page
    if not request.user.is_superuser:
       messages.error(request, 'Sorry, only store owners can do that.')
       return redirect(reverse('home'))
       
    # Prefilling the form using the product_object_or_404
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'{product.name} has been deleted!')
    return redirect(reverse('products'))
