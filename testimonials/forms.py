from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):

    class Meta:
        model = Testimonial
        fields = ('rtitle', 'rmessage', 'rrating')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        testimonials = Testimonial.objects.all()

        placeholders = {
            'rtitle': 'Testimonial Title',
            'rmessage': 'Type testimonial message here',
            'rrating': 'Rating',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False

            