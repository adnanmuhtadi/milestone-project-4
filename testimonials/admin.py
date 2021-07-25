from django.contrib import admin
from .models import Testimonial

# Register your models here.
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'user_profile',
        'user_test_title',
        'review_date',
        'rating',
    )

    ordering = ('review_date',)

admin.site.register(Testimonial, TestimonialAdmin)