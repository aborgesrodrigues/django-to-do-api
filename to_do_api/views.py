import logging

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from to_do_api.models import Task, User
from to_do_api.serializers import TasksSerializer, UserSerializer

logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer

   def list(self, request, *args, **kwargs):
      """
      Retrieve all users
      """
      logger.info("list")
      return super().list(request, *args, **kwargs)


class TaskViewSet(viewsets.ModelViewSet):
   queryset = Task.objects.all()
   serializer_class = TasksSerializer
