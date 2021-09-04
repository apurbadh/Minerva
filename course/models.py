from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Module(models.Model):
    name = models.CharField(max_length=255)
    type_of = models.IntegerField()
    value = models.TextField()
    
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

 