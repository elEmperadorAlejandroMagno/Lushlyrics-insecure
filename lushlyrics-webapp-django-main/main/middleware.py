from django.shortcuts import redirect
import re

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        path_auth = [
            '/login', 
            '/singup', 
            '/reset_password', 
            '/reset_password_done', 
            '/reset_password_complete', 
            '/reset_password_confirm',
            '/reset' # Expresion regular para reset_password_confirm    
        ]
        if not request.user.is_authenticated and request.path not in path_auth and not request.path.startswith('/reset/'):
            return redirect('/login')
        response = self.get_response(request)
        return response