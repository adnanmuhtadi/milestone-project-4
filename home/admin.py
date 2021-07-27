from django.contrib import admin
from .models import ContactUs

class ContactUsAdmin(admin.ModelAdmin):
    # How they would be displayed in the django admin
    list_display = (
        'user',
        'csubject',
        'cmessage',
        'cdate',
        'ctime',
    )

    # Ordering them in reverse in order of date
    ordering = ('-cdate','-ctime',)

admin.site.register(ContactUs, ContactUsAdmin)