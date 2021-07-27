from django.shortcuts import get_object_or_404, render
from django.conf import settings

from testimonials.models import Testimonial

# Create your views here.


def index(request):
    """ 
    A view to return the index page
    """
    # Taking the information from the testimonial app and then reversing the order of display
    testimonials = Testimonial.objects.all().order_by('-rdate')

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'home/index.html', context)

def refunds(request):
    """
    A view to return the returns page
    """

    return render(request, 'home/refunds.html')


def privacy(request):
    """ 
    A view to return the privacy page 
    """

    return render(request, 'home/privacy.html')


def terms(request):
    """ 
    A view to return the terms and conditions page 
    """

    return render(request, 'home/terms.html')


def about(request):
    """ 
    A view to return the about page 
    """
    gmaps_api = settings.GMAPS_API

    template = 'home/about.html'
    context = {
        'gmaps_api': gmaps_api,
    }

    return render(request, template, context)