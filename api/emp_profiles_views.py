from django.shortcuts import render
from rest_framework.views import APIView
from employee_profile.models import Employee_profile
from .serializers import EmployeeProfileSerializer
from rest_framework.response import Response
from rest_framework import status, generics
# Create your views here.

class EmployeeProfilesAll(APIView):
    queryset = Employee_profile.objects.all()
    serializer_class = EmployeeProfileSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class
        emp_profiles = self.queryset.all()

        return Response({"status": "success", "profiles": serializer(emp_profiles, many=True).data},
                        status=status)

class EmployeeProfileListApi(generics.ListAPIView):
    serializer_class = EmployeeProfileSerializer
    queryset = Employee_profile.objects.all()