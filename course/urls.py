from os import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("course/<int:id>", views.course, name="course"),
    path("course/<int:id>/forum", include("forum.urls"), name="forum"),
    path("login", views.loginPage, name="login"),
    path("register", views.registerPage, name="register"),
    path("verify", views.verifyPage, name="verify"),
    path("apply", views.verifyThePage, name="apply"),
    path("logout", views.logoutUser, name="logout"),
    path("change", views.changeProfile, name="change"),
    path("create-course", views.createCourse, name="createCourse"),
    path('search', views.search, name="search"),
    path('new', views.new, name="new")
]
