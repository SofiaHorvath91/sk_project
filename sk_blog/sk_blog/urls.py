"""sk_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('static.urls')),
    path('books/', include('books.urls', namespace='books')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('comments/', include('comments.urls', namespace='comments')),
    path('favourites/', include('favourites.urls', namespace='favourites')),
    path('feedbacks/', include('feedbacks.urls', namespace='feedbacks')),
    path('quizes/', include('quizes.urls', namespace='quizes')),
]

urlpatterns += staticfiles_urlpatterns()

