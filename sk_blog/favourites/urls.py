from django.urls import path
from .views import (
    favourite_create_view,
    favourite_delete_view,
)

app_name = 'favourites'

urlpatterns = [
    path('create/<int:id>', favourite_create_view, name='create'),
    path('delete/<int:id>', favourite_delete_view, name='delete'),
]