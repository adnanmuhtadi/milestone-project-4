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
        contactus = ContactUs.objects.all()

        placeholders = {
            'csubject': 'Subject',
            'cmessage': 'Message',
        }
        
        for field_name, field in self.fields.items():
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False
