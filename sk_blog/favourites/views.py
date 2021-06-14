from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Favourite
from comments.models import Comment
from books.models import Book


@login_required
def favourite_create_view(request, id):
    context = {}
    book = Book.objects.filter(id=id).first()
    context['book'] = book
    if request.method == "POST":
        name = book.title
        bookid = book.id
        user = request.user
        writer = book.writer
        published = book.published
        type = book.type
        series = book.series

        try:
            favourite_try = Favourite.objects.get(bookname=bookid)
            context['errorMsg'] = 'Book is already among your favourites'
            return render(request, 'favourites/create.html', context=context)
        except Favourite.DoesNotExist:
            favourite = Favourite.objects.create(name=name, bookname=bookid, writer=writer,
                                                 published=published, type=type, series=series, author=user)
            favourite.save()
            return redirect('books:detail', id=book.id)
    else:
        return render(request, 'favourites/create.html', context=context)


@login_required
def favourite_delete_view(request, id):
    context = {}
    favourite = Favourite.objects.filter(id=id).first()
    context['favourite'] = favourite
    if request.method == "POST":

        if request.user == favourite.author:
            favourite.delete()
            return redirect('accounts:favourites', username=favourite.author)
        else:
            return redirect('accounts:favourites', username=favourite.author)
    else:
        return render(request, 'favourites/delete.html', context=context)


