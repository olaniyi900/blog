from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('author_detail/', views.author_detail, name='author_detail'),
    path('<int:author_id>/author_profile/', views.author_profile, name='author_profile'),
    path('author_form_view/', views.author_form_view, name='author_form_view'),
    path('blog_form_view/', views.blog_form_view, name='blog_form_view'),
]