from django.db import models
from django.conf import settings
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering =['name']

    def __str__(self):
        return self.name
class Employee_profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user",
                             on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=25, default='')
    city = models.CharField(max_length=25, default='')
    department = models.ForeignKey(Department, related_name="department",
                                   on_delete=models.CASCADE, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name

