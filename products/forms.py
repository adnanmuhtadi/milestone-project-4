from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        # to define the model and it will include ALL the fields.
        model = Product
        exclude = ('has_sizes',)

    # Allowing the widget to be available for all 4 image inputs
    image = forms.ImageField(label='Image 1', required=False, widget=CustomClearableFileInput)
    imagetwo = forms.ImageField(label='Image 2', required=False, widget=CustomClearableFileInput)
    imagethree = forms.ImageField(label='Image 3', required=False, widget=CustomClearableFileInput)
    imagefour = forms.ImageField(label='Image 4', required=False, widget=CustomClearableFileInput)


    # to override the init method
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # having the categories show up in its readable name
        categories = Category.objects.all()
        # creating a list of readable names associated with the categories
        friendly_name = [(c.id, c.get_friendly_name()) for c in categories]
        

        # updating the category field in the form from the pulled list and instead of seeing the
        # category ID or the name field, we would see the friendly name
        self.fields['category'].choices = friendly_name
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
