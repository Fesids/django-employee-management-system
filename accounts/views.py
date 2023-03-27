from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy, reverse
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateResponseMixin, View
from employee_profile.models import Employee_profile
from api.serializers import EmployeeProfileSerializer
from .models import CustomUserModel
# Create your views here.

class HomePage(generic.TemplateView):
    template_name = 'home.html'


'''class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")'''

class SignUp(TemplateResponseMixin, View):
    template_name = "registration/signup.html"

    def get_formset(self, data=None):

        return CustomUserCreationForm(data=data)
    def get(self, request, format=None):
        form = self.get_formset()
        return self.render_to_response({
            "form": form
        })


    def post(self, request, format=None):
        form = self.get_formset(data=request.POST)

        if form.is_valid():
            form.save()

            data_emp = {
                "user": request.POST,
                "first_name": "",
                "last_name": "",
                "phone": "",
                "city": "",
                "department": None
            }
            emp = EmployeeProfileSerializer(data=data_emp)
            if emp.is_valid():
                emp.save()


            return redirect("login")

        return self.render_to_response({
            "form": form
        })
