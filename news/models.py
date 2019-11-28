from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    about_author = models.TextField()
    date_of_birth = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    


class Blog(models.Model):
    title = models.CharField(max_length=40)
    news_content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateField()
    
    def __str__(self):
        return self.title
    
