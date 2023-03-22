from django.urls import path
from .accounts_views import CustomModeListSerializer
from .emp_profiles_views import EmployeeProfilesAll, EmployeeProfileListApi

urlpatterns = [
    path("accounts/all/", CustomModeListSerializer.as_view()),

    # path("emp_profiles/all", EmployeeProfilesAll.as_view()),

    path("emp_profiles/all/", EmployeeProfileListApi.as_view())
]