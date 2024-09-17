from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:id>", views.detail, name="detail"),
    path("" , include("users.urls")),
]