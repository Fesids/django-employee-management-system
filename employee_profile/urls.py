from django.urls import path
from .views import CreateEmployeeProfile, ListEmployeeProfile, UpdateEmployeeProfile

urlpatterns= [
    path("new/", CreateEmployeeProfile.as_view(), name="employee_create"),
    path("", ListEmployeeProfile.as_view(), name="employee_list"),
    path("<int:pk>/", UpdateEmployeeProfile.as_view(), name="employee_update")
]