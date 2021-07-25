from django.contrib import admin
from .models import Testimonial

# Register your models here.
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'rtitle',
        'rdate',
        'rrating',
    )

    ordering = ('-rdate',)

admin.site.register(Testimonial, TestimonialAdmin)