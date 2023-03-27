from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Employee_profile, Department
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from django.db.models import Count
from django.http import HttpResponse
from .forms import UpdateEmployeeForm

class GenericMixin:
    def get_queryset(self):
        qs = self.get_queryset()
        return qs.filter()

class EmployeeProfileMixin(generic.View):
    model = Employee_profile
    fields = ['user', 'first_name','last_name', 'phone', 'city', 'department']
    success_url = reverse_lazy('employee_list')


class AdminUserProfileMixin(EmployeeProfileMixin, LoginRequiredMixin):
    model = Employee_profile
    object_context_name = "employee"
class CreateEmployeeProfile(AdminUserProfileMixin, generic.CreateView):

    template_name = 'employees/manage/create_employee.html'


class ListEmployeeProfile(generic.ListView):
    model = Employee_profile
    template_name = 'employees/manage/list_employee.html'

    def head(self, *args, **kwargs):
        last_employee = self.get_queryset().latest('created')

        response = HttpResponse(
            headers={
                last_employee.created.strftime('%a, %d %b %Y %H:%M:%S GMT')
            }
        )

        return response

'''class UpdateEmployeeProfile(AdminUserProfileMixin,generic.UpdateView):

    template_name = 'employees/manage/update_employee.html'''

class UpdateEmployeeProfile(TemplateResponseMixin, View):
    template_name = "employees/manage/update_employee.html"
    emp_profile = None

    def get_formset(self, data=None):
        return UpdateEmployeeForm(instance=self.emp_profile,data=data)

    def dispatch(self, request, pk, *args, **kwargs):
        self.emp_profile= get_object_or_404(Employee_profile, id=pk)
        return super().dispatch(request, pk)

    def get(self, request, format=None):
        formset = self.get_formset()
        return self.render_to_response({
            "employee": self.emp_profile,
            "form": formset
        })

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect("employee_list")

        return self.render_to_response({
            'employee': self.emp_profile,
            'form': formset
        })
class EmployeeProfileDetail(EmployeeProfileMixin, generic.DetailView):
    template_name = 'employees/manage/detail_employee.html'
    context_object_name = "employee"

class DeleteEmployeeProfile(AdminUserProfileMixin, generic.DeleteView):

    template_name = 'employees/manage/delete_employee.html'
    context_object_name = 'employee'