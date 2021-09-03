from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib import messages
from .decorators import not_loggedin

# Create your views here.
@login_required(login_url="/login")
def index(req):
    pass


@login_required(login_url="/login")
def course(req, name):
    pass

@not_loggedin
def loginPage(req):
    if req.method == "POST":
        username = req.POST["username"]
        password = req.POST["password"]
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('/')
        else:
            messages.error(req, "Username or Password Incorrect !")
            return redirect('/login')
    return render(req, "login.html")

@not_loggedin
def registerPage(req):
    if req.method == "POST":
        form = forms.UserForm(req.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            login(user)
            return redirect('/')
        else:
            errors = list(form.errors.values())          
            messages.error(req, errors[0])
            return redirect("/register")
    form = forms.UserForm()
    context = { "form" : form}
    return render(req, "register.html", context)


@login_required(login_url="/login")
def logoutUser(req):
    logout(req.user)
    return redirect('/login')