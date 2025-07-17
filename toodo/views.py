from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Profile, Task
from .serializers import ProfileSerializer, TaskSerializer
# Create your views here.

@api_view(['POST'])
def signup(request):
    try:
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Account created successfully"}, status=201)
        return Response(serializer.errors, status=400)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['POST'])
def task(request):
    try:
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Task created successfully"}, status=201)
        return Response(serializer.errors, status=400)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(['GET'])
def get_tasks(request, id):
    try:
        profile = Profile.objects.get(id=id)
        tasks = profile.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=200)
    except Profile.DoesNotExist:
        return Response({"error": "Profile not found"}, status=404)