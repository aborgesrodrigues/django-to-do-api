import logging

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from to_do_api.audit_logging import HTTPAuditLogger
from to_do_api.models import Task, User
from to_do_api.serializers import TasksSerializer, UserSerializer

logger = logging.getLogger(__name__)

audit_logger = HTTPAuditLogger.from_env()
audit_logger.start()


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer

   @audit_logger.log_inbound(include_request_in_response=False)
   def list(self, request, *args, **kwargs):
      """
      Retrieve all users
      """
      logger.info("list")
      return super().list(request, *args, **kwargs)

   @audit_logger.log_inbound(include_request_in_response=False)
   def create(self, request, *args, **kwargs):
      """
      Create a user
      """
      return super().create(request, *args, **kwargs)


class TaskViewSet(viewsets.ModelViewSet):
   queryset = Task.objects.all()
   serializer_class = TasksSerializer
