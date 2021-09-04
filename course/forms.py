from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models.base import Model
from django.forms.models import ModelForm
from .models import Course, Module

class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
class CourseForm(ModelForm):
    
    class Meta:
        model = Course
        fields = ["name", "description", "picture"]
        
        
class CKForm(ModelForm):
    
    class Meta:
        model = Module
        fields = ["name", "info", "text_store"]
        
class VideoForm(ModelForm):
    
    class Meta:
        model = Module
        fields = ["name", "info", "url_store"]
        
class QuizForm(ModelForm):
    
    class Meta:
        model = Module
        fields = ["name", "info", "quiz_store"]