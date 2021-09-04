from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import forms, models
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .decorators import not_loggedin, is_not_teacher, is_teacher
from .verify import getData, check_github

# Create your views here.
@login_required(login_url="/login")
def index(req):
    return render(req, "index.html")


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
            login(req, user)
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
    logout(req)
    return redirect('/login')

@login_required
@is_not_teacher
def verifyPage(req):
    if req.method == "POST":
        code = getData(req.user.email)
        req.session["code"] = str(code)
        return redirect("/apply")
    return render(req, "verify.html")

@login_required
@is_not_teacher
def verifyThePage(req):
    if req.method == "POST":
        actual_code = req.session.get("code")
        code = req.POST["code"]
        username = req.POST["username"]
        if str(code) == actual_code and check_github(username):
            group = Group.objects.get(name="teachers")
            req.user.groups.add(group)
            return redirect('/')
        messages.error("Invalid Information")
        return redirect("/apply")
    return render(req, "apply.html")


@login_required
def changeProfile(req):
    if req.POST == "POST":
        form = forms.UserForm(req.POST, instance=req.user)
        if form.is_valid():
            form.save()
            messages.success("Edited sucessfully !")
        else:
            errors = list(form.errors.values())          
            messages.error(req, errors[0])
        return redirect('/change')
    form = forms.UserForm(instance=req.user)
    context = {
        "form" : form
    }
    return render(req, "changepassword.html", context)

@is_teacher
def createCourse(req):
    if req.method == "POST":
        form = forms.CourseForm(req.POST, req.FILES)
        res = form.save(commit=False)
        res.teacher = req.user
        res.save()
        return redirect('/')
        
    form = forms.CourseForm()
    context = {
        "form":form
    }
    return render(req, "create-course.html", context)