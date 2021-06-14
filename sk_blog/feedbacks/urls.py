from django.urls import path
from .views import (
    feedback_create_view,
    feedback_created_view,
    feedback_delete_view,
)

app_name = 'feedbacks'

urlpatterns = [
    path('create/', feedback_create_view, name='create'),
    path('created/', feedback_created_view, name='created'),
    path('delete/<int:id>', feedback_delete_view, name='delete'),
]

