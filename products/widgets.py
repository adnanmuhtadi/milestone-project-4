from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    Inherts the built in widgets
    """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
    