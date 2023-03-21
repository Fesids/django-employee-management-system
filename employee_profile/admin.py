from django.contrib import admin
from .models import Employee_profile, Department
# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}


@admin.register(Employee_profile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'city']
    list_display = ['first_name', 'last_name', 'city', 'phone','created', 'updated']
    list_filter = ['created', 'updated', 'department']



