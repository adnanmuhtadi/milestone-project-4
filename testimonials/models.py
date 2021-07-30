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
    rating = models.IntegerField(
        null=True, blank=True, default=0)

    # String to return the review titles
    def __str__(self):
        return self.title
