from .permissions import IsAuthorOrReadOnly
from .serializers import EmployeeProfileSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from employee_profile.models import Employee_profile
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from employee_profile.models import Employee_profile


class EmployeeProfilesAll(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Employee_profile.objects.all()
    serializer_class = EmployeeProfileSerializer

class EmployeeProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Employee_profile.objects.all()
    serializer_class = EmployeeProfileSerializer


class EmployeeMixin:
    serializer_class = EmployeeProfileSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs

    def get_object(self,id):
        try:
            return Employee_profile.objects.get(id=id)
        except:
            return Response(status.HTTP_404_NOT_FOUND)


class EmployeeProfileDelete(APIView, EmployeeMixin):

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        employee = self.get_object(id)


        if(employee):

            try:

                employee.delete()

                return Response({"message": "deleted"}, status.HTTP_204_NO_CONTENT)


            except:
                return Response({"status": "something went wrong in deleting post"}, status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"status": f"employee_profile with id {id} don't exist"})

class EmployeeProfileCreate(APIView, EmployeeMixin):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "employee_profile": serializer.data}, status.HTTP_201_CREATED)

        else:
            return Response({"status": "fail", "message": serializer.errors}, status.HTTP_400_BAD_REQUEST)


class EmployeeProfileUpdate(APIView, EmployeeMixin):
    permission_classes = [AllowAny, ]
    def put(self, request, *args, **kwargs):
        id = self.kwargs.get("id")
        emp_profile = get_object_or_404(Employee_profile, id=id)

        if not emp_profile:
            return Response({"message": f"profile with id {id} doesn't exists"}, status.HTTP_400_BAD_REQUEST)

        data = {
            "user": request.data.get("user"),
            "first_name": request.data.get("first_name"),
            "last_name": request.data.get("last_name"),
            "phone": request.data.get("phone"),
            "city": request.data.get("city")
        }

        serializer = self.serializer_class(instance=emp_profile, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"body": serializer.data}, status.HTTP_200_OK)
        return Response({"message": serializer.errors}, status.HTTP_400_BAD_REQUEST)


