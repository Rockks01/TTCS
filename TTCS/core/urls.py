from django.urls import path, include
from .views import *

urlpatterns = [
    path("", Web.index, name="index"),
    path("signin", Web.signin, name="signin"),
    path("signup", Web.signup, name="signup"),
    path("profile", Web.profile, name="profile"),
    path("logout", Web.logout_user, name="logout_user"),

    path("tasks", Web.tasks, name="tasks"),
    path("rating", Web.rating, name="rating")
]

handler505 = "core.views"