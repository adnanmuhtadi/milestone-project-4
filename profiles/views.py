from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Returns the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    # if the request is post
    if request.method == 'POST':
        # create a new instance of the profile
        form = UserProfileForm(request.POST, instance=profile)
        # and if the form is valid, save and send a success message
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    # Populatring the view with the uses profiles information
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form':form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)