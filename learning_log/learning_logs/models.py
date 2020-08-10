from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    """A topic the user is learning about"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model in the overview of the admin panel"""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic"""

    """The foreignkey definition connects the entries to topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    """In the admin panel django would otherwise just add an 's' to Entry"""

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Return a string representation of the model in the overview of the admin panel"""
        if len(self.text) >= 50:
            text_displayed = f"{self.text[:50]}..."
        else:
            text_displayed = f"{self.text[:50]}"

        return text_displayed
