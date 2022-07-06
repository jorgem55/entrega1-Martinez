from django.db import models

# Create your models here.
class Members(models.Model):
    name=models.CharField(max_length=20)
    bike=models.CharField(max_length=20)
    buy_date = models.DateField(null=True)
    
    def __str__(self):
        return f'Member: {self.name}'
