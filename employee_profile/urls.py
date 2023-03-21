from django.urls import path
from .views import CreateEmployeeProfile

urlpatterns= [
    path("new/", CreateEmployeeProfile.as_view(), name="employee_create")
]