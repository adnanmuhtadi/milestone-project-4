from django import forms
from .models import ContactUs


class ContactForm(forms.ModelForm):

    class Meta:
        # To define the model and it will include ALL the fields.
        model = ContactUs
        fields = '__all__'

    # To override the init method
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
