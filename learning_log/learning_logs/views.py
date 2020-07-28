from django.shortcuts import render
from .models import Topic, Entry

# Create your views here.


def index(request):
    """The home page for learning Log"""
    return render(request, "learning_logs/index.html")


def topics(request):
    """The topics page for learning Log"""
    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)
