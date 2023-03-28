from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from employee_profile.models import Employee_profile, Department
from .models import CustomUserModel

user = CustomUserModel

@receiver(post_save, sender=user)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = CustomUserModel.objects.last()
        department = Department.objects.get(id=1)
        Employee_profile.objects.create(user=instance, first_name=user.username, last_name="unknown", phone="999999", city="unknown", department=department)