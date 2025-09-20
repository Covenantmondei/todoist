from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
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
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def get_tasks(request):
    try:
        auth_user = request.user

        profile = Profile.objects.get(id=auth_user.id)
        tasks = profile.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=200)
    except Profile.DoesNotExist:
        return Response({"error": "Profile not found"}, status=404)


@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def update_task(request, id):
    try:
        data = request.data
        title = data.get("title")
        description = data.get("description")
        time_scheduled = data.get("time_scheduled")

        tasks = Task.objects.get(id=id)
        # user = request.user
        tasks.title = title
        tasks.description = description
        tasks.time_scheduled = time_scheduled

        tasks.save()

        # user.title = title
        # user.description = description
        # user.time_scheduled = time_scheduled
        # user.save()
        return Response({"Message": "Task Updated Successfully"}, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)



class TodoManager(APIView):

    def post(self, request):
        try:
            user_id = request.resolver_match("id")
            user_profile = Profile.objects.get(id=user_id)

            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Task created successfully"}, status=201)
            return Response(serializer.errors, status=400)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        

    def get(self, request):
        try:
            id = request.resolver_match("id")
            profile = Profile.objects.get(id=id)
            tasks = profile.tasks.all()
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=200)
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=404)


    def put(self, request):
        try:
            id = request.resolver_match("id")
            data = request.data
            title = data.get("title")
            description = data.get("description")
            time_scheduled = data.get("time_scheduled")

            tasks = Task.objects.get(id=id)
            tasks.title = title
            tasks.description = description
            tasks.time_scheduled = time_scheduled

            tasks.save()
            return Response({"Message": "Task Updated Successfully"}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)