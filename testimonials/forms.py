from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):

    class Meta:
        # To define the model and it will include ALL the fields.
        model = Testimonial
        fields = ('title', 'message', 'rating')

    # To override the init method
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        placeholders = {
            'title': 'Testimonial Title',
            'message': 'Type testimonial message here',
            'rating': 'Rating 1 - 5',
        }

        # Only displaying the placeholder fields
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False
