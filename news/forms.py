from django.forms import ModelForm, Textarea, TextInput, DateInput, Select
from .models import Author, Blog



class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'about_author', 'date_of_birth']
        widgets = {
            'first_name':TextInput(attrs={'class': 'form-control'}),
            'last_name':TextInput(attrs={'class': 'form-control'}),
            'about_author':Textarea(attrs={'class': 'form-control'}),
            'date_of_birth':DateInput(attrs={'class': 'form-control', 'type':'date'}),
        }



class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'news_content', 'author', 'pub_date']
        widgets = {
            'title':TextInput(attrs={'class': 'form-control'}),
            'news_content':Textarea(attrs={'class': 'form-control'}),
            'author':Select(attrs={'class': 'form-control'}),
            'pub_date':DateInput(attrs={'class': 'form-control', 'type':'date'}),
        }
