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
    path("topics/", views.topics, name="topics"),
    # Detail page for a single topic
    path("topics/<int:topic_id>/", views.topic, name="topic"),
    # Page for adding a new topic
    path("new_topic/", views.new_topic, name="new_topic"),
    # Page for adding a new entry
    path("new_entry/<int:topic_id>/", views.new_entry, name="new_entry"),
    # New page for editing an entry
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
]
