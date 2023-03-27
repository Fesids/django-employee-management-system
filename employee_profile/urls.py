from django.urls import path
from .views import CreateEmployeeProfile, ListEmployeeProfile, UpdateEmployeeProfile, EmployeeProfileDetail, DeleteEmployeeProfile
from .teste_views import ProfileListTeste, CreateProfileTeste, SignUpTeste
urlpatterns= [
    path("new/", CreateEmployeeProfile.as_view(), name="employee_create"),
    path("", ListEmployeeProfile.as_view(), name="employee_list"),
    path("<int:pk>/", UpdateEmployeeProfile.as_view(), name="employee_update"),
    path("detail/<int:pk>/", EmployeeProfileDetail.as_view(), name="employee_detail"),
    path("delete/<int:pk>/", DeleteEmployeeProfile.as_view(), name="employee_delete"),




    # teste
    path("teste/list/", ProfileListTeste.as_view(), name="teste_list"),
    path("create/teste/",CreateProfileTeste.as_view(), name="create_teste"),
    path("teste/signup/", SignUpTeste.as_view(), name="signup_teste")
]