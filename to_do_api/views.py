from django.shortcuts import render

from rest_framework import viewsets

from to_do_api.serializers import UserSerializer, TasksSerializer
from to_do_api.models import User, Task


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
   queryset = Task.objects.all()
   serializer_class = TasksSerializer
