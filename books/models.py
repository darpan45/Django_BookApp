from django.db import models
from django.contrib.auth.models import User
import json

# Create your models here.
#darpan pass
#darpan2 pass@123

#passwords changed for both users - pass@321

class Author(models.Model):
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title=models.CharField(max_length=256)
    isbn=models.CharField(max_length=256)
    pageCount=models.IntegerField(default=0)
    publishedDate=models.DateTimeField(auto_now_add=True)
    thumbnailUrl=models.CharField(max_length=256,null=True)
    shortDescription=models.CharField(max_length=512,null=True,blank=True)
    longDescription=models.TextField(null=True)
    status=models.CharField(max_length=256)
    authors=models.ManyToManyField(Author)
    categories=models.CharField(max_length=256)

    def __str__(self):
        return self.title

class Review(models.Model):
    body=models.TextField()
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    created_at=models.DateTimeField(auto_now=True)
    book=models.ForeignKey(Book,on_delete=models.CASCADE,null=True)


