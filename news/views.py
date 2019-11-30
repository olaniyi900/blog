from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Author, Blog
from .forms import AuthorForm, BlogForm

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


def author_form_view(request):
    form = AuthorForm()
    context = {'form': form}
    author_data = AuthorForm(request.POST)
    if author_data.is_valid():
        d = author_data.save()
        return HttpResponseRedirect('/news/author_detail/')

    return render(request, 'news/authorform.html', context)


def blog_form_view(request):
    form = BlogForm()
    context = {'form': form}
    blog_data = BlogForm(request.POST)
    if blog_data.is_valid():
        b = blog_data.save()
        return HttpResponseRedirect('/news/')
    return render(request, 'news/blogform.html', context)
