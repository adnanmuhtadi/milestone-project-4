from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Testimonial
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

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'rtitle':
                sortkey = 'lower_rtitle'
                testimonials = testimonials.annotate(lower_rtitle=Lower('rtitle'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            testimonials = testimonials.order_by(sortkey)
            

    sorting_testimonials = f'{sort}_{direction}'

    context = {
        'testimonials': testimonials,
        'sorting_testimonials': sorting_testimonials,
    }

    return render(request, 'testimonials/testimonials.html', context)


def add_testimonial(request):
    """ Add a testimonial to the app """

    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()

            messages.success(request, f'Thank you for taking your time to write a review \
            Your testimonial has been add!')
            return redirect(reverse('testimonials'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = TestimonialForm()

    template = 'testimonials/add_testimonial.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_testimonial(request, testimonial_id):
    """ Edit a product in the store """
    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the testimonial!')
            return redirect(reverse('testimonials'))
        else:
            messages.error(request, 'Failed to update the testimonial. Please ensure the form is valid.')
    else:
        form = TestimonialForm(instance=testimonial)
        messages.info(request, f'You are editting the testimonial for {testimonial.rtitle}! ')

    template = 'testimonials/edit_testimonial.html'
    context = {
        'form': form,
        'testimonial': testimonial,
    }

    return render(request, template, context)


def delete_testimonial(request, testimonial_id):
    """ Delete a testimonial from the app """
    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    testimonial.delete()
    messages.success(request, 'The testimonial has been deleted!')
    return redirect(reverse('testimonials'))


