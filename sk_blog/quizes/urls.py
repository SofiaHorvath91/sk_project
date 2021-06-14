from django.urls import path
from .views import (
    quiz_create_view,
    quiz_question_view,
    quiz_list_view,
    quiz_detail_view,
    quiz_answer_view,
    quiz_answer_delete_view,
    quiz_question_delete_view,
    quiz_delete_view,
    quiz_update_view,
    quiz_question_update_view,
    quiz_answer_update_view,
    quiz_play_view,
    quiz_result_view,
    quiz_result_delete_view,
)

app_name = 'quizes'

urlpatterns = [
    path('create/', quiz_create_view, name='create'),
    path('list/', quiz_list_view, name='list'),
    path('detail/<str:quizname>', quiz_detail_view, name='detail'),
    path('delete_quiz/<str:quizname>', quiz_delete_view, name='delete_quiz'),
    path('update_quiz/<str:quizname>', quiz_update_view, name='update_quiz'),
    path('question/<str:quizname>', quiz_question_view, name='question'),
    path('delete_question/<str:quizname>/<int:questionID>', quiz_question_delete_view, name='delete_question'),
    path('update_question/<str:quizname>/<int:questionID>', quiz_question_update_view, name='update_question'),
    path('answer/<str:quizname>/<int:questionID>', quiz_answer_view, name='answer'),
    path('delete_answer/<str:quizname>/<int:questionID>/<int:answerID>', quiz_answer_delete_view, name='delete_answer'),
    path('update_answer/<str:quizname>/<int:questionID>/<int:answerID>', quiz_answer_update_view, name='update_answer'),
    path('play/<str:quizname>', quiz_play_view, name='play'),
    path('result/<int:id>', quiz_result_view, name='result'),
    path('delete_result/<int:id>', quiz_result_delete_view, name='delete_result'),
]