from django.urls import path, include
from .views import *

urlpatterns = [
    path("", Web.index, name="index"),
    path("signin", Web.signin, name="signin"),
    path("signup", Web.signup, name="signup"),
    path("profile", Web.profile, name="profile")
]

handler505 = "core.views"