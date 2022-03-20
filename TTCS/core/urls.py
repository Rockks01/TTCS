from django.urls import path, include
from .views import *

urlpatterns = [
    path("", Web.index, name="index"),
    path("signin", Web.signin, name="signin"),
    path("signup", Web.signup, name="signup"),
    path("profile", Web.profile, name="profile"),
    path("logout", Web.logout_user, name="logout_user"),

    path("tasks", Web.tasks, name="tasks"),
    path("rating", Web.rating, name="rating"),
    path("about_me", Web.about_me, name="about_me"),
    path("change_status", Web.change_status, name="change_status"),
    path("change_description", Web.change_description, name="change_description")
]

handler505 = "core.views"