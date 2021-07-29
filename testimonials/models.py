from django.db import models
from django.contrib.auth.models import User


class Testimonial(models.Model):
    """
    Testimonal modal which would display the fields required
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    title = models.CharField(max_length=254)
    message = models.TextField()
    rating = models.DecimalField(
        max_digits=1, decimal_places=0, null=True, blank=True)

    # String to return the review titles
    def __str__(self):
        return self.title
