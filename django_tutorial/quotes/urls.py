from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('quote/<int:quote_id>/', views.quote, name='detail'),
    path('book/<int:book_id>/', views.book, name='book'),
    path('author/<int:author_id>/', views.author, name='author')
]
