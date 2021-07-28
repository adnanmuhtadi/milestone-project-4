from django.contrib import admin
from .models import ContactUs


# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    # How they would be displayed in the django admin
    list_display = (
        'cuser',
        'csubject',
        'cmessage',
        'cdate',
        'ctime',
    )

    # Ordering them in reverse in order of date
    ordering = ('-cdate', '-ctime',)


admin.site.register(ContactUs, ContactUsAdmin)
