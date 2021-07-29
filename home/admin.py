from django.contrib import admin
from .models import ContactUs


# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    # How they would be displayed in the django admin
    list_display = (
        'user',
        'subject',
        'message',
        'date',
        'time',
    )

    # Ordering them in reverse in order of date
    ordering = ('-date', '-time',)


admin.site.register(ContactUs, ContactUsAdmin)
