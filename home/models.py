from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ContactUs(models.Model):

    class Meta:
        verbose_name_plural = 'Contact Us'

    cuser = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    csubject = models.CharField(max_length=254)
    cmessage = models.TextField()
    cdate = models.DateField(auto_now_add=True)
    ctime = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.csubject
