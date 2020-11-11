''' Models for the polls Django application '''
import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    ''' Model definition for the Question datapoint '''
    # models.CharField defines a field that takes any sort of string 'for-instance-this'
    # max_length is optional but we set it to 200!
    question_text = models.CharField(max_length=200)
    # models.DateTimeField defines a field that takes in a date-time formatted datapoint.
    pub_date = models.DateTimeField('date published')

    # This is how we want to display the instance of the question when we print it.
    # For instance: print(question) will display the question_text.
    def __str__(self):
        return self.question_text

    # Was published recently is a function that checks if the instance of question has
    # been published in the last day.
    def was_published_recently(self):
        ''' Checks if the pub_date of the question has been in the past day '''
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    ''' Model definition for the Choice datapoint '''

    # models.ForeignKey is a way to create a relationship between
    # two data points in the database. This ForeignKey creates
    # a one-to-many relationship between Choice and Question.
    # A question can have multiple choice instances with the foreignkey pointing to that question instance
    # but a choice can only point to one question instance.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # models.CharField defines a field that takes any sort of string 'for-instance-this'
    # max_length is optional but we set it to 200!
    choice_text = models.CharField(max_length=200)
    # Votes is an IntegerField, anything that's not an integer (e.g. 'a', 3.5, {'test': 'dictionary})
    # will cause it to throw an error. By defining a default value (0) we don't have to worry about
    # assigning a value to votes when first creating the Choice datapoint.
    # You can see this in the add_choice view - we don't define a vote value when adding
    # a new choice but it will still be created in the database with votes=0!
    votes = models.IntegerField(default=0)

    # This is how we want to display the instance of the question when we print it.
    # For instance: print(question) will display the question_text.
    # Try to remove this __str__ method to see what it displays!
    def __str__(self):
        return self.choice_text
