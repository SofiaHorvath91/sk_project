from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from books.models import Book
from comments.models import Comment
from favourites.models import Favourite
from feedbacks.models import Feedback
from quizes.models import Result

User = get_user_model()


def user_create_view(request):
    if request.method == "POST":
        context = {}
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            username = request.POST['username']
            email = request.POST['email']

            try:
                user1 = User.objects.get(username=username)
                context['errorMsg'] = 'Username is already in system'
                return render(request, 'accounts/create.html', context=context)
            except User.DoesNotExist:
                try:
                    user2 = User.objects.get(email=email)
                    context['errorMsg'] = 'Email is already in system'
                    return render(request, 'accounts/create.html', context=context)
                except User.DoesNotExist:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    return redirect('books:list')
        else:
            context['errorMsg'] = 'Passwords must match'
            return render(request, 'accounts/create.html', context=context)
    else:
        return render(request, 'accounts/create.html')


def user_login_view(request):
    if request.method == "POST":
        context = {}
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            context['successMsg'] = 'Successful login'
            return render(request, 'accounts/login.html', context=context)
        else:
            context['errorMsg'] = 'Invalid login'
            return render(request, 'accounts/login.html', context=context)
    else:
        return render(request, 'accounts/login.html')


def user_logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'accounts/logout.html')
    else:
        return redirect('accounts/login.html')


def user_profile_view(request, username):
    context = {}
    user = User.objects.get(username=username)
    context['user'] = user
    return render(request, 'accounts/profile.html', context=context)


def user_favourites_view(request, username):
    context = {}
    user = User.objects.get(username=username)
    favourites = Favourite.objects.filter(author=user)
    context['favourites'] = favourites
    return render(request, 'accounts/favourites.html', context=context)


def user_comments_view(request, username):
    context = {}
    user = User.objects.get(username=username)
    comments = Comment.objects.filter(author=user)
    context['comments'] = comments
    return render(request, 'accounts/comments.html', context=context)


def user_feedbacks_view(request, username):
    context = {}
    user = User.objects.get(username=username)
    feedbacks = Feedback.objects.filter(author=user)
    context['feedbacks'] = feedbacks
    return render(request, 'accounts/feedbacks.html', context=context)


def user_results_view(request, username):
    context = {}
    user = User.objects.get(username=username)
    results = Result.objects.filter(player=user)
    context['results'] = results
    return render(request, 'accounts/results.html', context=context)