from django.shortcuts import redirect

def not_loggedin(func):
    
    def wrapper(req, *args, **kwargs):
        if req.user.is_authenticated:
            return redirect('/')
        return func(req, *args, **kwargs)
    
    return wrapper