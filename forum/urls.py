from os import name
from django.urls import path
from . import views

urlpatterns = [
   path("<int:id>", views.forum, name="question~"),
   path("question/<int:id>", views.answers, name="answer") 
]
