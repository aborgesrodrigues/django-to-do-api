import uuid
from enum import Enum

from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)


class TaskState(Enum):
    TO_DO = 1
    DOING = 2
    DONE = 3


class Task(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    description = models.CharField(max_length=100)
    state = models.CharField(max_length=10)
    user_id = models.UUIDField()
