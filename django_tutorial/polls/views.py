import datetime

from django.shortcuts import render, get_object_or_404
from django.template import loader
# Create your views here.
from .models import Question, Choice
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(question.choice_set.all())
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def create(request):
    question = Question(
        question_text=request.POST.get('question_text'),
        pub_date=datetime.datetime.now()
    )
    question.save()
    return HttpResponseRedirect(reverse('polls:index'))


def add_choice(request, question_id):
    try:
        question = Question.objects.get(id=question_id)

    except Question.DoesNotExist:
        return render(request, 'todo/task_list.html', {
            'error_message': "The task list does not exist"
        })

    choice = Choice(
        question=question,
        choice_text=request.POST.get('choice_text')
    )
    choice.save()
    return HttpResponseRedirect(reverse('polls:detail', args=(question_id,)))


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
