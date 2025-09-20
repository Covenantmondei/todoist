from django.urls import path
from .views import *

urlpatterns = [
    path("signup", signup, name="signup"),
    path("create-task", task, name="task"),
    path("tasks/<int:id>", get_tasks, name="get_tasks"),
    path("update/<int:id>", update_task, name="update task"),
    path("manager/<int:id>", TodoManager.as_view(), name="tasks")
]