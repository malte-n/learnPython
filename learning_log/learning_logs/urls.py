"""Defines URL patterns for learning_logs"""
from django.urls import path

from . import views

app_name = "learning_logs"

urlpatterns = [
    # Home page
    # 1. Argument is a URL string to route
    # 2. which function to call in views.py (in this case index())
    # 3. The name of the URL to refer to in other parts of this app
    path("", views.index, name="index"),
    # Page that shows all topics
    # path("topics/", views.topics, name="topics"),
]
