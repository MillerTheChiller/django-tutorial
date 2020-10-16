from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Quote
# Create your views here.


def index(request):
    quotes_list = Quote.objects.all()
    print(quotes_list)
    template = loader.get_template('quotes/index.html')
    context = {'quote_list': quotes_list}
    return HttpResponse(template.render(context, request))


def quote(request, quote_id):
    return HttpResponse("You're looking at the quote %s." % quote_id)


def book(request, book_id):
    response = "You're looking at the book %s."
    return HttpResponse(response % book_id)


def author(request, author):
    return HttpResponse("You're looking at the author %s." % author)
