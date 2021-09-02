from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("course/<slug:name>", views.course, name="course"),
    path("course/<slug:name>/forum", include("forum.urls"), name="forum"),
    path("course/<slug:name>/quiz/", include("quiz.urls"), name="quiz"),
    
]
