from django.db import models
import json

# Create your models here.
#darpan pass
#darpan2 pass@123
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
    created_at=models.DateTimeField(auto_now=True)
    book=models.ForeignKey(Book,on_delete=models.CASCADE,null=True)


