from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from accounts.models import Profile


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'id']

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ['user.username']

class TasksSerializer(serializers.ModelSerializer):
	user = UserSerializer(many=False, read_only=True)
	profile = ProfileSerializer(many=True, read_only=True)
	class Meta:
		model = Task
		fields = '__all__'
