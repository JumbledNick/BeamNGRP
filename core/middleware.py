from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

class lockdownMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            return self.get_response(request)
        
        login_url = reverse("login")

        if request.path == login_url:
            return self.get_response(request)
        if request.path.startswith("/admin/"):
            return self.get_response(request)
        if request.path.startswith("/static/"):
            return self.get_response(request)
        
        return redirect("login")