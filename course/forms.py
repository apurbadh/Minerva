from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm
from .models import Course

class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
class CourseForm(ModelForm):
    
    class Meta:
        model = Course
        fields = "__all__"