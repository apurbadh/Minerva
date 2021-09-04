from os import name
from django.db import models
from django.contrib.auth.models import User
from course.models import Course

# Create your models here.
class Question(models.Model):
    question = models.TextField()
    user = models.ForeignKey(User, name="quser", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, name="course", on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.question

class Answer(models.Model):
    user = models.ForeignKey(User, name="user", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, name="question", on_delete=models.CASCADE)
    answer = models.TextField()
    
    def __str__(self) -> str:
        return self.answer
    



    