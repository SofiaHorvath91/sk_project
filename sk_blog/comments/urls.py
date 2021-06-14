from django.urls import path
from .views import (
    comment_create_view,
    comment_delete_view,
    comment_update_view,
)

app_name = 'comments'

urlpatterns = [
    path('create/<int:id>', comment_create_view, name='create'),
    path('delete/<int:id>', comment_delete_view, name='delete'),
    path('update/<int:id>', comment_update_view, name='update')
]

