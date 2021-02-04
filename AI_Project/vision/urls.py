from django.urls import path
from vision import views

urlpatterns = [
    path("", views.home, name="home"),
    path("vision/<name>", views.hello_there, name="hello_there")
]