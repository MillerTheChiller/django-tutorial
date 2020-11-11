import os
import datetime
from django.core.management.base import BaseCommand
from polls.models import Question, Choice


class Command(BaseCommand):

    def _create_poll(self):
        Question(
            question_text='Who is your favourite musician?',
            pub_date=datetime.datetime.now()
        ).save()

        print("***** ADDING TEST QUESTION TO THE DATABASE *****")

    def _create_choices(self):
        question = Question.objects.get(id=1)
        Choice(
            question=question,
            choice_text='Billy Eyelash'
        ).save()
        Choice(
            question=question,
            choice_text='BLACKPINK'
        ).save()
        Choice(
            question=question,
            choice_text='Clairo'
        ).save()
        Choice(
            question=question,
            choice_text='Dua Lipa'
        ).save()
        Choice(
            question=question,
            choice_text='Taylor Swift'
        ).save()

        print("***** ADDING TEST CHOICES TO THE DATABASE *****")

    def handle(self, *args, **options):
        self._create_poll()
        self._create_choices()
