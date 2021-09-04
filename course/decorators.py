from django.contrib import messages
from django.shortcuts import redirect
from .models import Course

def not_loggedin(func):
    
    def wrapper(req, *args, **kwargs):
        if req.user.is_authenticated:
            return redirect('/')
        return func(req, *args, **kwargs)
    
    return wrapper

def is_not_teacher(func):
    def wrapper(req, *args, **kwargs):

        if not req.user.is_authenticated or req.user.groups.filter(name="teachers"):
            messages.error(req, "You are already a teacher")
            return redirect('/')  
        return func(req, *args, **kwargs)
    
    return wrapper


def is_teacher(func):
    
    def wrapper(req, *args, **kwargs):
        if not req.user.is_authenticated or not req.user.groups.filter(name="teachers"):
            return redirect('/')  
        return func(req, *args, **kwargs)
    
    return wrapper
