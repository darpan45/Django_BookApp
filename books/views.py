from django.shortcuts import render
from django.http import HttpResponse
import json

booksData=open(r'C:\Users\Darpan\Desktop\Projects\Django 2021\Django-Course\bookstore-Project\books.json').read()

data=json.loads(booksData)

def index(request):
    #render function searches for templates folder in the app
    context={'books':data}
    return render(request,'books/index.html',context)

def book_details(request,id):
    singleBook=[]
    for book in data:
        if book['id']==id:
            singleBook=book
    context={'book':singleBook}
    return render(request,'books/book_details.html',context)