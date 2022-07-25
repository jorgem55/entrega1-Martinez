from datetime import datetime
from django.db import models
class Members(models.Model):
    name=models.CharField(max_length=20)
    bike=models.CharField(max_length=20)
    buy_date = models.DateField(null=True)
    
    def __str__(self):
        return f'Member: {self.name}'

class Posts(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField(max_length=500)
    author=models.CharField(max_length=20)
    creation_date = models.DateField(datetime.now())
    
    def __str__(self):
        return f'Post: {self.name}'