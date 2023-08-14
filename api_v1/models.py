from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Log(models.Model):
    """Model for a Log object"""
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    filename = models.CharField(max_length=255)
    datetime_adding_log = models.DateTimeField(auto_now_add=True)
    datetime_creating_log = models.DateTimeField()
    log = models.TextField()

    class Meta:
        ordering = ('-datetime_adding_log', )

    def __str__(self):
        return f'{filename} - {self.datetime_creating_log}: "{self.log}"'
