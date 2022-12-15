from rest_framework import serializers

from to_do_api.models import User, Task

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ('id', 'name', 'username')


class TasksSerializer(serializers.ModelSerializer):
   class Meta:
       model = Task
       fields = ('id', 'description', 'state', 'user_id')