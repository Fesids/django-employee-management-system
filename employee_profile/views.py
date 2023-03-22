from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Employee_profile, Department
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from django.db.models import Count

class GenericMixin:
    def get_queryset(self):
        qs = self.get_queryset()
        return qs.filter()

class EmployeeProfileMixin(generic.View):
    model = Employee_profile
    fields = ['user', 'first_name','last_name', 'phone', 'city', 'department']
    success_url = reverse_lazy('employee_list')

class CreateEmployeeProfile(EmployeeProfileMixin, generic.CreateView):

    template_name = 'employees/manage/create_employee.html'


class ListEmployeeProfile(generic.ListView):
    model = Employee_profile
    template_name = 'employees/manage/list_employee.html'

class UpdateEmployeeProfile(EmployeeProfileMixin,generic.UpdateView):
    fields = ['user', 'first_name', 'last_name', 'phone', 'city', 'department']
    success_url = reverse_lazy('employee_list')
    template_name = 'employees/manage/update_employee.html'

class EmployeeProfileDetail(EmployeeProfileMixin, generic.DeleteView):
    template_name = 'employees/manage/detail_employee.html'