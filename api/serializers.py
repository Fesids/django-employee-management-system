from accounts.models import CustomUserModel
from employee_profile.models import Employee_profile
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUserModel
        fields = '__all__'


class EmployeeProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee_profile
        fields = '__all__'