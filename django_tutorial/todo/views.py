from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template import loader
from .models import Task, TaskList
# Create your views here.


def index(request):
    task_lists = TaskList.objects.all().order_by('-id')
    template = loader.get_template('todo/index.html')
    context = {'task_lists': task_lists}
    return HttpResponse(template.render(context, request))


def task_list(request, task_list_id):
    try:
        task_list = TaskList.objects.get(id=task_list_id)
    except TaskList.DoesNotExist:
        raise Http404('This task list does not exist.')
    tasks = Task.objects.filter(task_list=task_list_id).order_by('-id')
    template = loader.get_template('todo/task_list.html')

    context = {'task_list': task_list, 'tasks': tasks}
    return HttpResponse(template.render(context, request))


def task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        raise Http404('This task does not exist.')

    return HttpResponse("You're looking at the task %s." % task_id)


def create_task_list(request):
    task_list = TaskList(
        list_title=request.POST.get('list_title'),
        list_description=request.POST.get('list_description')
    )
    task_list.save()
    return HttpResponseRedirect(reverse('tasks:index'))


def create_task(request, task_list_id):
    try:
        task_list = TaskList.objects.get(id=task_list_id)

    except TaskList.DoesNotExist:
        return render(request, 'todo/task_list.html', {
            'error_message': "The task list does not exist"
        })

    task = Task(
        task_list=task_list,
        task_title=request.POST.get('task_title'),
        do_by=request.POST.get('do_by') or None
    )
    task.save()

    return HttpResponseRedirect(reverse('tasks:task-list', args=(task_list_id,)))
