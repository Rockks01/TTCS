from django.urls import path, include
from .views import *

urlpatterns = [
    path("", Web.index, name="index")
]

handler505 = "core.views"