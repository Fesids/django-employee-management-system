from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUserModel
# Register your models here.

@admin.register(CustomUserModel)
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUserModel
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ['email', 'username', 'is_active', 'is_staff', 'is_superuser']
    search_fields = ['email', 'username']
