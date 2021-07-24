from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        # Meta option to tell django which model it will be associated to
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            # Dictionary of placeholders which will show up in the form
            'default_phone_number': 'Phone Number',
            'default_address_line1': 'Street Address 1',
            'default_address_line2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county_state': 'County or State',
            'default_postcode': 'PostCode',
        }

        # Set the full name with the autofocus attribute so the cursor
        # would begin in that area of the form when the page is loaded
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    # * added a '*' if the field is mandatory
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # Setting the placeholder attributes to their values
                # in the dictionary above
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # CSS class which is used in base.css
            self.fields[field].widget.attrs['class'] = 'border-black round-0 profile-form-input'
            # Removing the form field labels
            self.fields[field].label = False
