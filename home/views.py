from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
# This is for the secret keys in the settings
from django.conf import settings
# Django imports to help with sending emails
from django.core.mail import send_mail
from django.template.loader import render_to_string

from testimonials.models import Testimonial
from profiles.models import UserProfile
from .forms import ContactForm

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


def contact(request):
    """
    A view to show the contact page
    """

    return render(request, 'home/contact.html')


def send_email(request):
    """
    Send the site admin an email using the contact form
    """
    # To check if the request method is post, and then to get all the filed elements
    # in the contact form and store them in the variables
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # checking if the form is a valid
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()

            messages.success(request, f'Thank you for taking your time to write a review \
            Your testimonial has been add!')
            # On success, redirect the user to the testimonials home page
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ContactForm()

    template = 'home/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)