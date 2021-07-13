
from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    idno=models.AutoField(primary_key=True)
    book_name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    genre=models.CharField(max_length=200)
    language=models.CharField(max_length=200)

# Create your models here.
