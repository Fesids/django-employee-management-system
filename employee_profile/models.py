from django.db import models
from django.conf import settings
# Create your models here.

class Employee_profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user",
                             on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=25, default='')
    city = models.CharField(max_length=25, default='')

    def __str__(self):
        return self.first_name
