from django.urls import path
from .accounts_views import CustomModeListSerializer

urlpatterns = [
    path("accounts/all/", CustomModeListSerializer.as_view()),
]