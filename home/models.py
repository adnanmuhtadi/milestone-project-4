from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ContactUs(models.Model):

    class Meta:
        verbose_name_plural = 'Contact Us'

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=254)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
