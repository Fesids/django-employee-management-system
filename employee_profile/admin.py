from django.contrib import admin
from .models import Employee_profile
# Register your models here.

@admin.register(Employee_profile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    model = Employee_profile


