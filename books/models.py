from django.db import models
import json

# Create your models here.
#darpan pass
class Book(models.Model):
    title=models.CharField(max_length=256)
    isbn=models.CharField(max_length=256)
    pageCount=models.IntegerField(default=0)
    publishedDate=models.DateTimeField(auto_now_add=True)
    thumbnailUrl=models.CharField(max_length=256,null=True)
    shortDescription=models.CharField(max_length=512,null=True,blank=True)
    longDescription=models.TextField(null=True)
    status=models.CharField(max_length=256)
    authors=models.CharField(max_length=256)
    categories=models.CharField(max_length=256)

    def __str__(self):
        return self.title