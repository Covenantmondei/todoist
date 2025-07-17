from rest_framework import serializers
from .models import Profile, Task

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def create(self, validated_data):
        profile = Profile.objects.create(**validated_data)
        return profile


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['created_at']

    def create(self, validated_data):
        task = Task.objects.create(**validated_data)
        profile = validated_data.get('profile')
        if profile:
            profile.number_of_tasks += 1
            profile.save()
        return task