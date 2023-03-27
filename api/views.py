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
        emp_profiles = self.queryset()

        return Response({"status": "success", "profiles": serializer(emp_profiles, many=True).data},
                        status=status)


class EmployeeProfileDetail(APIView):
    queryset = Employee_profile.objects.all()
    serializer_class = EmployeeProfileSerializer
    post = None
    def dispatch(self, request, *args, **kwargs):
        id = self.kwargs.get('id')
        self.post = Employee_profile.objects.filter(id=id)

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class

        return Response({"status": "success", "post":serializer(self.post, many=True).data}, status=status.HTTP_200_OK)