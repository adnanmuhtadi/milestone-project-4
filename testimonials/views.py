from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Testimonial
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .forms import TestimonialForm

# Create your views here.

def all_testimonials(request):
    """ 
    A view to return all the testimonials made by users
    """

    testimonials = Testimonial.objects.all()
    sort = None
    direction = None

    # Checking if request.GET exists
    if request.GET:
        if 'sort' in request.GET:
            # Allowing sort to equals sortkey
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'rtitle':
                sortkey = 'lower_rtitle'
                # Annotate the list of products with the new field
                testimonials = testimonials.annotate(lower_rtitle=Lower('rtitle'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                # Check if the direction is descending or ascending
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            # To sort the testimonials
            testimonials = testimonials.order_by(sortkey)
            

    sorting_testimonials = f'{sort}_{direction}'

    context = {
        'testimonials': testimonials,
        'sorting_testimonials': sorting_testimonials,
    }

    return render(request, 'testimonials/testimonials.html', context)


@login_required
def add_testimonial(request):
    """ 
    Add a testimonial to the app
    """

    # Checking if the request method is post
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        # checking if the form is a valid
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()

            messages.success(request, f'Thank you for taking \
                your time to write a review \
            Your testimonial has been add!')
            # On success, redirect the user to the testimonials home page
            return redirect(reverse('testimonials'))
        else:
            messages.error(request, 'Failed to add product. Please \
                ensure the form is valid.')
    else:
        form = TestimonialForm()

    template = 'testimonials/add_testimonial.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_testimonial(request, testimonial_id):
    """ 
    Edit a product in the store
    """
    # Prefilling the form using the product_object_or_404
    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    if request.method == 'POST':
        # Checking if the request method is post, telling the instance to
        # post new information of that instance of the testimonial.
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the testimonial!')
            return redirect(reverse('testimonials'))
        else:
            messages.error(request, 'Failed to update the testimonial. \
                Please ensure the form is valid.')
    else:
        # Creating the instance of the testimonial form
        form = TestimonialForm(instance=testimonial)
        messages.info(request, f'You are editting the testimonial \
            for {testimonial.rtitle}! ')

    # Informing it which template to use.
    template = 'testimonials/edit_testimonial.html'
    context = {
        'form': form,
        'testimonial': testimonial,
    }

    return render(request, template, context)


@login_required
def delete_testimonial(request, testimonial_id):
    """ 
    Delete a testimonial from the app
    """
    # Prefilling the form using the product_object_or_404
    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    testimonial.delete()
    messages.success(request, 'The testimonial has been deleted!')
    return redirect(reverse('testimonials'))


