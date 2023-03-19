from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUserModel
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUserModel
        fields = UserCreationForm.Meta.fields + ("email",)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUserModel
        fields = UserChangeForm.Meta.fields