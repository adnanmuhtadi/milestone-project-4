from django.shortcuts import render
from .models import Testimonial

# Create your views here.

def all_testimonials(request):
    """ 
    A view to return all the testimonials made by users
    """

    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'testimonials/testimonials.html', context)