from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def index_view(request):
    return render(request, 'base.html')


def sports_view(request):
    return render(request, 'sports.html')


def news_view(request):
    return render(request, 'news.html')


def pagen_view(request, n):
    print(reverse('pgn_url', args=[300]))
    return HttpResponse('this is %s page' % n)


def test_static(request):
    return render(request, 'test_static.html')


def index2_view(request):
    return render(request, 'index.html')
