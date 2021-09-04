from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Quiz(models.Model):
    questions = models.TextField()
    options = models.TextField()

class Module(models.Model):
    name = models.CharField(max_length=255)
    type_of = models.IntegerField() 
    info = models.TextField()
    text_store = RichTextField(null=True, blank=True)
    url_store = models.CharField(max_length=255,null=True)
    quiz_store = models.ForeignKey(Quiz, related_name="quiz", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    users = models.ManyToManyField(User, related_name="users")
    modules = models.ManyToManyField(Module, related_name="module")
    teacher = models.ForeignKey(User, related_name="teacher", on_delete=models.CASCADE, null=True)
    picture = models.ImageField()

    def __str__(self):
        return self.name
