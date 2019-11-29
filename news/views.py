from django.shortcuts import render, get_object_or_404
from .models import Author, Blog

def index(request):
    latest_news = Blog.objects.order_by('-pub_date')
    context = {'latest_news': latest_news}

    return render(request, 'news/index.html', context)

def home(request):
    return render(request, 'base.html')


def author_detail(request):
    author_info = Author.objects.all()

    context = {'author_info': author_info}
    return render(request, 'news/author_detail.html', context)

def author_profile(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    context = {'author': author}
    return render(request, 'news/author_profile.html', context)
