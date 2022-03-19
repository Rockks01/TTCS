import sys

from django.shortcuts import render

class Web:
    def index (request):
        if not request.user.is_authenticated:
            return render(request, "index.html")
        else:
            return render(request, "profile.html")

    def signin(request):
        return render(request, "signin.html")

    def signup(request):
        return render(request, "signup.html")

def handler505(request):
    type_, value, traceback = sys.exc_info()
    data: dict = dict(value=value)
    return render(request, "error.html", data)