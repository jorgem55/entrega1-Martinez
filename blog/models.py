from django.db import models
from ckeditor.fields import RichTextField

class Members(models.Model):
    name=models.CharField(max_length=20)
    bike=models.CharField(max_length=20)
    buy_date = models.DateField(null=True)
    
    def __str__(self):
        return f'Member: {self.name}'

class Posts(models.Model):
    title=models.CharField(max_length=20)
    # subtitle=models.CharField(max_length=20)
    content=RichTextField(null=True)
    author=models.CharField(max_length=20)
    creation_date = models.DateField(null=True)
    # image = models.ImageField(upload_to='images', null=True, blank=True)
    
    def __str__(self):
        return f'Post: {self.title}'