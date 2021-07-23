from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Returns the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    # Populatring the view with the uses profiles information
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form':form,
        'orders': orders,
    }

    return render(request, template, context)