from django.db import models

# Create your models here.


class TaskList(models.Model):
    list_title = models.CharField(max_length=200)
    list_description = models.CharField(max_length=200)

    def __str__(self):
        return self.list_title


class Task(models.Model):
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=200)
    do_by = models.DateTimeField(null=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task_title
