from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from comments.models import Comment
from favourites.models import Favourite

@login_required
def book_create_view(request):
    if request.method == "POST":
        context = {}
        title = request.POST['title']
        writer = request.POST['writer']
        published = request.POST['published']
        series = request.POST['series']
        content = request.POST['content']
        quote1 = request.POST['quote1']
        quote2 = request.POST['quote2']
        quote3 = request.POST['quote3']
        funfact = request.POST['funfact']
        type = request.POST['type']
        image = ""

        if "'" in title or "," in title or ": " in title or "/" in title:
            if "'" in title:
                image = title.lower().replace("'", "")
            if "," in title:
                image = title.lower().replace(",", "")
            if ": " in title:
                image = title.lower().replace(": ", "")
            if "/" in title:
                image = title.replace("/", "")
        else:
            image = title.lower()

        if title and content and writer and published and series and type and image:
            user = request.user
            book = Book.objects.create(title=title, content=content, writer=writer, published=published,
                                       series=series, author=user, type=type, image=image,
                                       quote1=quote1, quote2=quote2, quote3=quote3, funfact=funfact)
            book.save()
            return redirect('books:detail', id=book.id)
        else:
            context['errorMsg'] = 'None of the fields should be empty'
            return render(request, 'books/create.html', context=context)
    else:
        return render(request, 'books/create.html')


@login_required
def book_delete_view(request, id):
    book = Book.objects.filter(id=id).first()
    comments = Comment.objects.filter(book=book.title)
    favourites = Favourite.objects.filter(author=book.author)
    if request.user == book.author:
        if request.method == "POST":
            book.delete()
            comments.delete()
            favourites.delete()
            return redirect('books:list')
        else:
            return render(request, 'books/delete.html')
    else:
        return redirect('books:list')


def book_detail_view(request, id):
    context = {}
    book = Book.objects.filter(id=id).first()
    comments = Comment.objects.filter(book=book.title)
    context['books'] = book
    context['comments'] = comments
    return render(request, 'books/detail.html', context=context)


def book_list_view(request):
    context = {}
    books = Book.objects.all().order_by('published')
    context['books'] = books
    context['countNovel'] = books.filter(type="Novel").count()
    context['countCollection'] = books.filter(type="Collection").count()
    context['countNonFiction'] = books.filter(type="Non-fiction").count()
    return render(request, 'books/list.html', context=context)


@login_required
def book_update_view(request, id):
    context = {}
    book = Book.objects.filter(id=id).first()
    context['book'] = book
    if request.user == book.author:
        if request.method == "POST":
            title = request.POST['title']
            writer = request.POST['writer']
            published = request.POST['published']
            series = request.POST['series']
            content = request.POST['content']
            quote1 = request.POST['quote1']
            quote2 = request.POST['quote2']
            quote3 = request.POST['quote3']
            funfact = request.POST['funfact']
            type = request.POST['type']
            image = ""

            if "'" in title or "," in title or ": " in title or "/" in title:
                if "'" in title:
                    image = title.lower().replace("'", "")
                if "," in title:
                    image = title.lower().replace(",", "")
                if ": " in title:
                    image = title.lower().replace(": ", "")
                if "/" in title:
                    image = title.replace("/", "")
            else:
                image = title.lower()

            if title and content and writer and published and series and image and type:
                book.title = title
                book.image = image
                book.content = content
                book.writer = writer
                book.published = published
                book.series = series
                book.type = type
                book.quote1 = quote1
                book.quote2 = quote2
                book.quote3 = quote3
                book.funfact = funfact

                book.save()
                return redirect('books:detail', id=book.id)
            else:
                context['errorMsg'] = 'Your title and content cannot be empty'
                return render(request, 'books/update.html', context=context)
        else:
            return render(request, 'books/update.html', context=context)
    else:
        return redirect('books:list')
