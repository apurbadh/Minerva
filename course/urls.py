from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("course/<slug:name>", views.course, name="course"),
    path("course/<slug:name>/forum", include("forum.urls"), name="forum"),
    path("course/<slug:name>/quiz/", include("quiz.urls"), name="quiz"),
    path("login", views.loginPage, name="login"),
    path("register", views.registerPage, name="register"),
    path("logout", views.logout, name="logout")
]
