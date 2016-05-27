from django.db import models
import uuid

class Task(models.Model):
    description = models.CharField(max_length=200)
