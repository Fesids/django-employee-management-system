from django import forms
from .models import Employee_profile


class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee_profile
        fields = ['user','first_name', 'last_name', 'city', 'phone', 'department']


class UpdateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee_profile
        fields = ['first_name', 'last_name', 'city', 'phone', 'department']