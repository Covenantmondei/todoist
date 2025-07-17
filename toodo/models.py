from django.db import models

# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    number_of_tasks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    time_scheduled = models.DateTimeField(blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title