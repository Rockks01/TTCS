import sys
import hashlib
from datetime import datetime as dt

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from django.contrib.auth.models import User

class Web:
    def index (request):
        if not request.user.is_authenticated:
            return render(request, "index.html")
        else:
            return render(request, "profile.html")

    def signin(request):
        if not request.user.is_authenticated:
            return render(request, "signin.html")

    def signup(request):
        print(request.user.is_authenticated)
        if not request.user.is_authenticated:
            data: dict = dict()
            if "register-button" in request.POST:
                username: str = request.POST["username"]
                email: str = request.POST["email"]
                password: str = request.POST["password"]

                if not username or not email or not password:
                    message: str = "Поля не должны оставаться пустыми!" # Set message.
                    data["message"] = message
                else:
                    hash_password: str = hashlib.md5(password.encode("utf-8")).hexdigest() # Convert password to md5 hash.
                    user = User.objects.filter(username=username).exists() # Check user.
                    if not user:
                        user = User.objects.create(username=username, email=email, password=hash_password, is_staff=False) # Create new user.
                        login(request, user) # Auth user in the system.
                        return redirect("profile") # Redirect to 'profile' page.
                    else:
                        message: str = "Пользователь с таким юзернейм существует!" # Set message.
                        data["message"] = message # Convert data to dict object.
            return render(request, "signup.html", data) # Render login page with data.
        else:
            return redirect("profile")

    def profile(request):
        print(request.user.is_authenticated)
        if request.user.is_authenticated:
            return render(request, "profile.html")

def handler505(request):
    type_, value, traceback = sys.exc_info()
    data: dict = dict(value=value)
    return render(request, "error.html", data)