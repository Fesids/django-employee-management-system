from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy, reverse
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateResponseMixin, View
from employee_profile.models import Employee_profile
from api.serializers import EmployeeProfileSerializer
from employee_profile.forms import CreateEmployeeForm
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
    user = None

    def get_formset(self, data=None):

        return CustomUserCreationForm(data=data)


    def get(self, request, format=None):
        form = self.get_formset()
        return self.render_to_response({
            "form": form
        })


    def post(self, request, format=None):
        form = self.get_formset(data=request.POST)

        '''data_emp = {
            "user": CustomUserModel.objects.last(),
            "first_name": "",
            "last_name": "",
            "phone": "",
            "city": "",
            "department": None
        }

        form_emp = self.get_formset_employee(data=data_emp)'''

        if form.is_valid():
            user = form.save()
            # employee = Employee_profile.objects.create(user=user)


            return redirect("login")

        return self.render_to_response({
            "form": form
        })
