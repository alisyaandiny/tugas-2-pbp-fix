from django.db import models
from django.contrib.auth.models import User

class TaskItem(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
    is_finished = models.BooleanField(default=False)

# test