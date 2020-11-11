''' Specific views for the polls application! Handles CRUD operations and renders templates '''
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice


def index(request):
    ''' index view, the one you see when you go to the url /polls/. Handles a read operation '''
    # Get the latest questions, this gets all of the questions ordered descending by the pub_date
    # and takes the first five
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # make a context dictionary and add latest_question_list
    # these lines are the same as:
    # return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})
    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    ''' detail view, handle a read operation for a specific question '''
    # Am easy way to look up an object in the database or throw a 404 error if it is not found.
    # looks up the Questionss defined in the database for a question with the primary_key equal
    # to the one defined in the url
    # /polls/1 would look like: get_object_or_404(Question, pk=1)
    question = get_object_or_404(Question, pk=question_id)
    # Renders the polls/detail.html page with the context being the question we have found.
    # We could define context before this and have it like:
    # context = {'question': question}
    # render(request, 'polls/detail.html', context)
    # That would be the same functionality ^
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    ''' results view, handle a read operation for a specific question '''
    # An easy way to look up an object in the database or throw a 404 error if it is not found.
    # looks up the Questionss defined in the database for a question with the primary_key equal
    # to the one defined in the url
    # /polls/1/results would look like: get_object_or_404(Question, pk=1)
    question = get_object_or_404(Question, pk=question_id)
    # Renders the polls/results.html page with the context being the question we have found.
    # We could define context before this and have it like:
    # context = {'question': question}
    # render(request, 'polls/results.html', context)
    # That would be the same functionality ^
    return render(request, 'polls/results.html', {'question': question})


def create(request):
    ''' Create view, handle a create operation for a Question '''
    # Instantiate a Question object, question_text being the input that we have gathered from the POST request
    # and pub_date being automatically added.
    question = Question(
        question_text=request.POST.get('question_text'),
        pub_date=datetime.datetime.now()
    )
    # Save the question to the database
    question.save()
    # Redirect to polls index,
    # polls(from urls.py app_name):index(from the name we defined in the url that routes to views.index)
    return HttpResponseRedirect(reverse('polls:index'))


def add_choice(request, question_id):
    ''' A view that handles a create operation to a Choice datapoint '''
    # See if a question defined from the url exists in the database
    # /polls/1/add_choice would have the question_id of 1.
    try:
        question = Question.objects.get(id=question_id)
    # If the question does not exist render polls/index.html with an error message in the context.
    except Question.DoesNotExist:
        return render(request, 'polls/index.html', {
            'error_message': "The poll you tried to add a choice to does not exist"
        })
    # If the question does exist:
    # make a new Choice Object with the question as the foreign key,
    # and the choice_text being the choice_text you are getting from the POST request.
    choice = Choice(
        question=question,
        choice_text=request.POST.get('choice_text')
    )
    # Save to the database
    choice.save()
    # Redirect to the detail view - the namespacing here is:
    # polls(from urls.py app_name):detail(from the name we defined in the url that routes to views.detail)
    # args=(question_id,) sends over the question in the redirect as well, (variable,) is just the syntax for args.
    return HttpResponseRedirect(reverse('polls:detail', args=(question_id,)))


def vote(request, question_id):
    ''' A view that handles an Update operation to a Choice datapoint '''
    # get_object_or_404 checks the database for an object and if it isn't found returns a 404 error.
    question = get_object_or_404(Question, pk=question_id)
    try:
        # look in question.choice_set (the choices with the foreign key pointing to the question)
        # and see if the choice from the POST request exists.
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # If a ChoiceDoesNotExist error is thrown add an error_message to the render context and re-render the page.
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # If a choice does exist:
        # Adding a vote to the selected_choice and then saving the choice to the database.
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
