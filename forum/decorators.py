from django.shortcuts import redirect
from course.models import Course

def is_enrolled(func):
    
    def wrapper(req, id, *args, **kwargs):
        try:
            course = Course.objects.get(id=id).all()
        except:
            return redirect('/')
        if not req.user.is_authenticated or not req.user in course:
            return redirect('/')  
        return func(req, *args, **kwargs)
    
    return wrapper
