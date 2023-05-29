from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import SignUpForm
from django.contrib import messages
import logging



# Create your views here.
class SignUpView(FormView):
    template_name = 'accounts/signup.html'      # specifies the name of the template for rendering the signup form.
    form_class = SignUpForm                     # specifies the form (SignUpForm) used in the template. 
    redirect_authenticated_user = True          # is set to True to redirect the user once authenticated.
    success_url = reverse_lazy('home:index')    # specifies the URL to redirect once the user signs up successfully. In this example, it redirects the user to the index on home page.

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    

class LogInView(LoginView):
    template_name = 'accounts/login.html'  
    LoginView.form_class.template_name = 'accounts/form.html'

    def get_success_url(self):
        return reverse_lazy('home:index')

class LogOutView(LogoutView):
    next_page = reverse_lazy('accounts:login')


def password_change(request):
    template = 'accounts/password_change.html'
    context = {}
    return render(request, template, context)

def password_change_done(request):
    template = 'accounts/password_change_done.html'
    context = {}
    return render(request, template, context)

def password_reset(request):
    template = 'accounts/password_reset.html'
    context = {}
    return render(request, template, context)

def password_reset_done(request):
    template = 'accounts/password_reset_done.html'
    context = {}
    return render(request, template, context)

def password_reset_confirm(request):
    template = 'accounts/password_reset_confirm.html'
    context = {}
    return render(request, template, context)

def password_reset_complete(request):
    template = 'accounts/password_reset_complete.html'
    context = {}
    return render(request, template, context)
