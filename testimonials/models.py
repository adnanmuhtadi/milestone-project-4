from django.db import models

from profiles.models import UserProfile


class Testimonial(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True)
    review_date = models.DateTimeField(auto_now_add=True)
    user_test_title = models.CharField(max_length=254)
    user_message = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.user_test_title
