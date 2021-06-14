from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import (
    user_create_view,
    user_login_view,
    user_logout_view,
    user_profile_view,
    user_comments_view,
    user_favourites_view,
    user_feedbacks_view,
    user_results_view,
)

app_name = 'accounts'

urlpatterns = [
    path('create/', user_create_view, name='create'),
    path('login/', user_login_view, name='login'),
    path('logout/', user_logout_view, name='logout'),
    path('<str:username>/', user_profile_view, name='profile'),
    path('favourites/<str:username>', user_favourites_view, name='favourites'),
    path('comments/<str:username>', user_comments_view, name='comments'),
    path('feedbacks/<str:username>', user_feedbacks_view, name='feedbacks'),
    path('results/<str:username>', user_results_view, name='results'),
]