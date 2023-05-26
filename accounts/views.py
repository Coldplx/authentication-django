from django.shortcuts import render


# Create your views here.

def index(request):
    template = 'accounts/index.html'
    context = {}
    return render(request, template, context)

def login(request):
    template = 'accounts/login.html'
    context = {}
    return render(request, template, context)

def logout(request):
    template = 'accounts/logout.html'
    context = {}
    return render(request, template, context)

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
