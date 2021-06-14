from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Comment
from books.models import Book


@login_required
def comment_create_view(request, id):
    context = {}
    book = Book.objects.filter(id=id).first()
    context['book'] = book
    if request.method == "POST":
        booktitle = book.title
        content = request.POST['content']

        if content:
            user = request.user
            comment = Comment.objects.create(book=booktitle, content=content, author=user)
            comment.save()
            return redirect('books:detail', id=book.id)
        else:
            context['errorMsg'] = 'Comment should not be empty'
            return render(request, 'comments/create.html', context=context)
    else:
        return render(request, 'comments/create.html', context=context)


@login_required
def comment_delete_view(request, id):
    comment = Comment.objects.filter(id=id).first()
    book = Book.objects.filter(title=comment.book).first()
    context = {'book': book}
    if request.method == "POST":
        comment.delete()
        return redirect('books:detail', id=book.id)
    else:
        return render(request, 'comments/delete.html', context=context)


@login_required
def comment_update_view(request, id):
    context = {}
    comment = Comment.objects.filter(id=id).first()
    book = Book.objects.filter(title=comment.book).first()
    context['book'] = book
    context['comment'] = comment
    if request.method == "POST":
        content = request.POST['content']

        if content:
            comment.content = content
            comment.save()
            return redirect('books:detail', id=book.id)
        else:
            context['errorMsg'] = 'Your comment cannot be empty'
            return render(request, 'comments/update.html', context=context)
    else:
        return render(request, 'comments/update.html', context=context)
