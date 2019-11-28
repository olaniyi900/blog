from django.shortcuts import render
from .models import Author, Blog

def index(request):
    latest_news = Blog.objects.order_by('-pub_date')
    context = {'latest_news': latest_news}

    return render(request, 'news/index.html', context)
