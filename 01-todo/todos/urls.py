# todos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todo/<int:pk>/toggle/", views.toggle_complete, name="toggle_complete"),
    path("todo/<int:pk>/delete/", views.delete_todo, name="delete_todo"),
    path("todo/<int:pk>/edit/", views.edit_todo, name="edit_todo"),
]
