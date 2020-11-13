''' Urls for the polls application, comes here after the url is matched from /polls/ '''
from django.urls import path

from . import views

# After the urls.py file in django_tutorial has matched the url /polls/ it comes here:
# If the question_id was 1 this is how the url would be routed:
# /polls/ -> views.index
# /polls/create -> views.create
# /polls/1/ -> views.detail
# /polls/1/add_choice -> views.add_choice
# /polls/1/results/ -> views.results
# /polls/1/vote/ -> views.vote

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/add_choice', views.add_choice, name='add_choice'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
