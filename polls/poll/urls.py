from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    #http://127.0.0.1:8000/index/
    path("", views.poll_list, name='poll_list'),

    #http://127.0.0.1:8000/poll/1
    path("<int:question_id>/", views.detail, name='detail'),

    #http://127.0.0.1:8000/poll/1/
    path("<int:question_id>/vote/", views.vote, name='vote'),

    #http://127.0.0.1:8000/poll/test/
    path("test/", views.test),
]