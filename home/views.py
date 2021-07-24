from django.shortcuts import render

# Create your views here.


def index(request):
    """ 
    A view to return the index page
    """

    return render(request, 'home/index.html')


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
