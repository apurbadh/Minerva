from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    users = models.ManyToManyField(User, related_name="users")
    teacher = models.OneToOneField(User, related_name="teacher", on_delete=models.CASCADE)
    picture = models.ImageField()

class Module(models.Model):
    name = models.CharField(max_length=255)
    course = models.OneToOneField(Course, related_name="course", on_delete=models.CASCADE)
    type_of = models.IntegerField()
    value = models.TextField()
    