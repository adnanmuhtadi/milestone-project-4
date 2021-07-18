from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def delivery(request):
    """ A view to return the shipping and returns page """

    return render(request, 'home/delivery.html')


def privacy(request):
    """ A view to return the privacy page """

    return render(request, 'home/privacy.html')


def tandc(request):
    """ A view to return the terms and conditions page """

    return render(request, 'home/tandc.html')
