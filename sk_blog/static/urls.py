from django.urls import path
from .views import (
    home_view,
    kingverse_view,
    about_view
)


urlpatterns = [
    path('', home_view, name='home'),
    path('kingverse/', kingverse_view, name='kingverse'),
    path('about/', about_view, name='about'),
]