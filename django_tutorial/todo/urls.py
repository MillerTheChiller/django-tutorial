from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name="index"),
    path('todo/<int:task_list_id>', views.task_list, name="task-list"),
    path('todo/<int:task_list_id>/create',
         views.create_task, name="create-task")
]
