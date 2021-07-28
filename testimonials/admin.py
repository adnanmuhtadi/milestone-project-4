from django.contrib import admin
from .models import Testimonial


# Register your models here.
class TestimonialAdmin(admin.ModelAdmin):
    # How they would be displayed in the django admin
    list_display = (
        'user',
        'rtitle',
        'rrating',
        'rdate',
    )

    # Ordering them in reverse in order of date
    ordering = ('-rdate',)


admin.site.register(Testimonial, TestimonialAdmin)
