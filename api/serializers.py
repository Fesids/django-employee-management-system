from accounts.models import CustomUserModel
from employee_profile.models import Employee_profile, Department
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUserModel
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeProfileSerializer(serializers.ModelSerializer):
    # department = DepartmentSerializer(many=True, read_only=True)
    class Meta:
        model = Employee_profile
        fields = '__all__'