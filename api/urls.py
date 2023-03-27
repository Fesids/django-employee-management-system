from django.urls import path
from .accounts_views import CustomModeListSerializer, CustomModelDetailSerializer
from .emp_profiles_views import EmployeeProfilesAll, EmployeeProfileDetail, EmployeeProfileDelete, EmployeeProfileCreate, EmployeeProfileUpdate
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("accounts/all/", CustomModeListSerializer.as_view()),
    path("accounts/all/<int:pk>/", CustomModelDetailSerializer.as_view()),

    path("employee_profile/all/", EmployeeProfilesAll.as_view()),
    path("employee_profile/all/<int:pk>/", EmployeeProfileDetail.as_view()),
    path("employee_profile/all/delete/<int:id>", EmployeeProfileDelete.as_view()),
    path("employee_profile/all/update/<int:id>", EmployeeProfileUpdate.as_view()),
    path("employee_profile/new/", EmployeeProfileCreate.as_view()),

    # token path
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", jwt_views.TokenRefreshView.as_view(), name="token_refresh")
]