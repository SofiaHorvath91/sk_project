from django.urls import path
from .views import (
    book_create_view,
    book_list_view,
    book_delete_view,
    book_detail_view,
    book_update_view,
)

app_name = 'books'

urlpatterns = [
    path('create/', book_create_view, name='create'),
    path('list/', book_list_view, name='list'),
    path('delete/<int:id>', book_delete_view, name='delete'),
    path('detail/<int:id>', book_detail_view, name='detail'),
    path('update/<int:id>', book_update_view, name='update'),
]