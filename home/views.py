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
from .models import ContactUs

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
    # If request method is post, then it will get all of the
    # contact form info and store them in the vars
    if request.method == 'POST':
        cuser = request.user
        cfullname = request.POST['cfullname']
        cemail = request.POST['cemail']
        csubject = request.POST['csubject']
        cmessage = request.POST['cmessage']

        # Body var is using the render to string method and
        # passing the values to the contact email body text file
        # to the format i have specified
        body = render_to_string(
            'home/cemails/cemail_body.txt',
            {'username': cuser, 'fullname': cfullname,
             'message': cmessage, 'user_email': cemail,
             'subject': csubject})

        # Django send mail method, structure has to be
        # subject, message, from email and to email
        send_mail(
            f'This is the related {csubject}',
            body,
            cemail,
            [settings.DEFAULT_FROM_EMAIL],
        )

        # Message informing user using toasts that the message
        # has sent and redirecting them to the home page
        messages.success(
            request, 'Your message has been sent to the site admin')

        form = ContactForm(request.POST)
        print("form above")
        # checking if the form is a valid
        if form.is_valid():
            print(form)
            print("form valid")
            ContactUs = form.save(commit=False)
            ContactUs.cuser = request.user
            ContactUs.save()

            messages.success(request, f'Thank you for taking your time to write a review \
            Your testimonial has been add!')
            # On success, redirect the user to the testimonials home page

        else:
            print("form invalid")
            print(form.errors)
            messages.error(request, 'It has not been posted to the db')
            
        return redirect(reverse('home'))
    else:
        # Message informing user using toasts that the message
        # failed to send to the admin and redirecting them back
        # to the contact form
        messages.error(
            request, 'Failed to send message to admin')
        return redirect(reverse('contact'))

        form = ContactForm()

    template = 'home/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)