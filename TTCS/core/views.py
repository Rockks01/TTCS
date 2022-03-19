import sys
import hashlib
from datetime import datetime as dt

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .models import *

class Web:
    def index (request):
        if not request.user.is_authenticated:
            return render(request, "index.html")
        else:
            return redirect("profile")

    def signin(request):
        if not request.user.is_authenticated:
            data: dict = dict()
            if "login-button" in request.POST:
                email: str = request.POST["email"]
                password: str = request.POST["password"]
                if not email or not password:
                    message: str = "Поля не должны оставаться пустыми!" # Set message.
                    data["message"] = message
                else:
                    hash_password: str = hashlib.md5(password.encode("utf-8")).hexdigest() # Convert password to md5 hash.
                    user = CustomUser.objects.filter(email=email, password=hash_password) # Create user object from db.
                    if user.exists():
                        user = user.get() # Get user object from db.
                        user.last_login = dt.now() # Update datetime in last_login.
                        user.save() # Save changes.
                        login(request, user) # Auth user in the system.
                        return redirect("profile") # Redirect to 'profile' page.
                    else:
                        message: str = "Пользователь не существует!" # Set message.
                        data["message"] = message # Convert data to dict object.
            return render(request, "signin.html", data)

    def signup(request):
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
                    user = CustomUser.objects.filter(username=username).exists() # Check user.
                    if not user:
                        user = CustomUser.objects.create(username=username, email=email, password=hash_password, is_staff=False) # Create new user.
                        login(request, user) # Auth user in the system.
                        return redirect("profile") # Redirect to 'profile' page.
                    else:
                        message: str = "Пользователь с таким юзернейм существует!" # Set message.
                        data["message"] = message # Convert data to dict object.
            return render(request, "signup.html", data) # Render login page with data.
        else:
            return redirect("profile")

    def profile(request):
        if request.user.is_authenticated:
            return render(request, "profile.html")
        else:
            return redirect("profile")

    def logout_user(request):
        logout(request)
        return redirect("index")

    def tasks(request):
        return render(request, "tasks.html")

    def rating(request):
        return render(request, "rating.html")

def handler505(request):
    type_, value, traceback = sys.exc_info()
    data: dict = dict(value=value)
    return render(request, "error.html", data)