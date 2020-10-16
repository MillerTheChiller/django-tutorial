from django.contrib import admin

from .models import Quote, Book, Author

# Register your models here.


admin.site.register(Quote)
admin.site.register(Book)
admin.site.register(Author)
