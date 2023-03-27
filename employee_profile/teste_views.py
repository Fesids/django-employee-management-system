from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View, generic
from django.views.generic.base import TemplateResponseMixin
from .models import Employee_profile
from accounts.models import CustomUserModel
from .forms import CreateEmployeeForm
from accounts.forms import CustomUserCreationForm


class ProfileListTeste(generic.View):
    profs = Employee_profile.objects.all()

    def get(self, request):
        return render(request, "teste/teste_list.html", {"employees": self.profs})



class CreateProfileTeste(TemplateResponseMixin,generic.View):

    template_name = 'teste/teste_create_employee.html'
    employee_profile = None

    def get_formset(self, data=None):
        return CreateEmployeeForm(data=data)

    def get(self, request, *args, **kawrgs):
        formset = self.get_formset()
        return self.render_to_response({
            'form': formset
        })

    def post(self, request, format=None):


        formset = self.get_formset(data=request.POST)


        if formset.is_valid():
            formset.save()
            return redirect("teste_list")

        return self.render_to_response({
            'form': formset
        })



class SignUpTeste(TemplateResponseMixin, View):
    template_name = "teste/signup_teste.html"

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
            return redirect("login")

        return self.render_to_response({
            "form": form
        })





