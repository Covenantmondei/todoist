from django.urls import path
from .views import *

urlpatterns = [
    path("signup", signup, name="signup"),
    path("create-task", task, name="task"),
    path("tasks/<int:id>", get_tasks, name="get_tasks"),
]