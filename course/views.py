from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import forms, models
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .decorators import not_loggedin, is_not_teacher, is_teacher
from .verify import getData, check_github
from django.db.models import Q


# Create your views here.
@login_required(login_url="/login")
def index(req):
    course_user = []
    if not req.user.groups.filter(name="teachers"):
        courses = models.Course.objects.all()
        for course in courses:
            if req.user in course.users.all():
                course_user.append(course)
    else:
        course_user = models.Course.objects.all().filter(teacher=req.user)
    context = {
        "courses":course_user
    }
    return render(req, "index.html", context)

@login_required(login_url="/login")
def course(req, id):        
    try:
        course = models.Course.objects.get(id=id)
        if req.user not in course.users.all() and req.user != course.teacher:
            return redirect("/")
    except:
        course = None
    try:
        modules = course.modules.all()
    except:
        modules = None
    return render(req, "course.html", {"course":course, "modules" : modules})

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

@login_required(login_url="/login")
@is_not_teacher
def verifyPage(req):
    if req.method == "POST":
        code = getData(req.user.email)
        req.session["code"] = str(code)
        return redirect("/apply")
    return render(req, "verify.html")

@login_required(login_url="/login")
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
        messages.error(req, "Invalid Information")
        return redirect("/apply")
    return render(req, "apply.html")


@login_required(login_url="/login")
def changeProfile(req):
    if req.method == "POST":
        print("Here")
        username = req.POST["username"]
        email = req.POST["email"]
        password = req.POST["password"]
        user = User.objects.get(id=req.user.id)
        user.set_password(password)
        user.username = username
        user.email = email
        user.save()
        login(req, user)
        messages.success(req, "Edited sucessfully !")
        return redirect('/change')

    return render(req, "changepassword.html")

@is_teacher
@login_required(login_url="/login")
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

@login_required(login_url="/login")
def search(req):
    try:
        q = req.GET.get('q')
    except :
        return redirect('/')
    results = models.Course.objects.all().filter(Q(name__contains=f"{q}") | Q(description__contains=q))
    return render(req,'search.html',{'results':results})

@login_required(login_url="/login")
def new(req):
    courses=models.Course.objects.all()
    context = {
        "courses":courses
    }
    return render(req, "new.html", context)

@login_required(login_url="/login")
def enroll(req):
    if req.method == "POST":
        id = int(req.POST["course"])
        course = models.Course.objects.get(id=id)
        course.users.add(req.user)
    return redirect('/')

@login_required(login_url="/login")
def createmodule(req, id, type):
    course = models.Course.objects.get(id=id)
    if type not in ["text", "video", "quiz"] or req.user != course.teacher:
        return redirect("/")
    if type == "text":
        form = forms.CKForm()
    elif type == "video":
        form = forms.VideoForm()
    else:
        form = forms.QuizForm()
    context = {
        "form" : form
    }
    if req.method == "POST":
        if type == "text":
            form = forms.CKForm(req.POST, req.FILES)
            t = 1
        elif type == "video":
            form = forms.VideoForm(req.POST)
            t = 2
        else:
            form = forms.QuizForm(req.POST)
            t = 3
        if form.is_valid():
            res = form.save(commit=False)
            res.type_of = t
            res.save()
            course.modules.add(res)
            return redirect('/')
        
    return render(req, "createmodule.html", context)


@login_required(login_url="/login")
def module(req, id):
    try:
        course = models.Course.objects.get(id=id)
        modules = course.modules.all()
    except:
        return redirect('/')
    return render(req, "module.html", {"modules":modules})