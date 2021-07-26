from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):

    class Meta:
        # To define the model and it will include ALL the fields.
        model = Testimonial
        fields = ('rtitle', 'rmessage', 'rrating')

    # To override the init method
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Having the testimonials data all show up
        testimonials = Testimonial.objects.all()

        placeholders = {
            'rtitle': 'Testimonial Title',
            'rmessage': 'Type testimonial message here',
            'rrating': 'Rating',
        }

        # Only displaying the placeholder fields
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False

            