from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        # Meta option to tell django which model it will be associated to
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'address_line1', 'address_line2',
                  'town_or_city', 'county_state', 'postcode', 'country',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            # Dictionary of placeholders which will show up in the form
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'PostCode',
            'town_or_city': 'Town or City',
            'address_line1': 'Street Address 1',
            'address_line2': 'Street Address 2',
            'county_state': 'County or State',
        }

        # Set the full name with the autofocus attribute so the cursor
        # would begin in that area of the form when the page is loaded
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    # * added a '*' if the field is mandatory
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # Setting the placeholder attributes to their values
                # in the dictionary above
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # CSS class which is used in base.css
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Removing the form field labels
            self.fields[field].label = False
