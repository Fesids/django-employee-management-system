from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy, reverse
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Create your views here.

class HomePage(generic.TemplateView):
    template_name = 'home.html'

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")