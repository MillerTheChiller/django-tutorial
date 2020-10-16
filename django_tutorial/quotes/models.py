from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)
    wiki_link = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    goodreads_link = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Quote(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quote = models.CharField(max_length=2000)

    def __str__(self):
        return self.quote
