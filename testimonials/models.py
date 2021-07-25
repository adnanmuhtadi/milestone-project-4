from django.db import models
from django.contrib.auth.models import User


class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    rdate = models.DateTimeField(auto_now_add=True)
    rtitle = models.CharField(max_length=254)
    rmessage = models.TextField()
    rrating = models.DecimalField(max_digits=1, decimal_places=0, null=True, blank=True)

    def __str__(self):
        return self.rtitle
