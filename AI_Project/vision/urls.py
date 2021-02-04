from django.urls import path
from vision import views
from .views import polls_list, polls_detail

urlpatterns = [
    path("", views.home, name="home"),
    path("vision/<name>", views.hello_there, name="hello_there"),
    path("polls/", polls_list, name="polls_list"),
    path("polls/<int:pk>/", polls_detail, name="polls_detail")
]