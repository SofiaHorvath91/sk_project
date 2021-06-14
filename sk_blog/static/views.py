import os
import random
from django.shortcuts import render


def home_view(request):
    context = {}
    with open('static_files/txt/quotes.txt') as f:
        lines = [x.rstrip() for x in f]

    quoteNum = random.randint(0, (len(lines)-1))
    picNum = random.randint(1, 4)
    context['quote'] = lines[quoteNum]
    context['picNum'] = picNum
    return render(request, 'static/home.html', context=context)


def kingverse_view(request):
    context = {}
    return render(request, 'static/kingverse.html', context=context)


def about_view(request):
    context = {}
    return render(request, 'static/about.html', context=context)