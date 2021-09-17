from django.shortcuts import render, redirect, reverse
from django.contrib import messages
# This is for the secret keys in the settings
from django.conf import settings
# Django imports to help with sending emails
from django.core.mail import send_mail
from django.template.loader import render_to_string

from testimonials.models import Testimonial
from .forms import ContactForm

# Create your views here.


def index(request):
    """
    A view to return the index page
    """
    # Taking the information from the testimonial app and then reversing
    # the order of display
    testimonials = Testimonial.objects.all().order_by('-date')

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
    # If request method is post, then it will get the contact form info
    # and store them in the variables
    if request.method == 'POST':
        user = request.user
        contact_fullname = request.POST['contact_fullname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # The variables for the body using the render to string method and
        # passing the values to the email body text file
        body = render_to_string(
            'home/emails/email_body.txt',
            {'username': user, 'fullname': contact_fullname,
             'message': message, 'user_email': email,
             'subject': subject})

        # Django send mail method, structure
        send_mail(
            f'This is the related {subject}',
            body,
            email,
            [settings.DEFAULT_FROM_EMAIL],
        )

        form = ContactForm(request.POST)
        print("form above")
        # checking if the form is a valid
        if form.is_valid():
            print(form)
            print("form valid")
            ContactUs = form.save(commit=False)
            ContactUs.contact_user = request.user
            ContactUs.save()

            messages.success(request, 'Thank you for reaching out, your email \
                has been sent and will get back to you shortly')

        else:
            print("form invalid")
            print(form.errors)
            messages.error(request, 'It has not been posted to the database')

        return redirect(reverse('home'))
    else:
        # Message informing the user an issue occured and redirects
        # them to the home page
        messages.error(
            request, 'Failed to send the message to the administrator')
        return redirect(reverse('contact'))

        form = ContactForm()

    template = 'home/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
