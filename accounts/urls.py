from .views import SignUp
from django.urls import path

urlpatterns = [
    # path("home/", HomePage.as_view(), name="home"),
    path("signup/", SignUp.as_view(), name="signup")

]