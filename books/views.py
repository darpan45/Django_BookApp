from django.http.response import Http404
from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
from .models import Book,Review
#booksData=open(r'C:\Users\Darpan\Desktop\Projects\Django 2021\Django-Course\bookstore-Project\books.json').read()

#data=json.loads(booksData)

def index(request):
    #render function searches for templates folder in the app
    dbdata=Book.objects.all()
    context={'books':dbdata}
    return render(request,'books/index.html',context)

def book_details(request,id):
    try:
        singleBook=Book.objects.get(pk=id)
        #adding minus sign will make reviews in descending order
        reviews=Review.objects.filter(book_id=id).order_by('-created_at')
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    context={'book':singleBook,'reviews':reviews}
    return render(request,'books/book_details.html',context)

def review(request,id):
    #since form is sending post request,need to handle post request
    body = request.POST.get('review', False)
    newReview=Review(body=body,book_id=id) #entering values in db just like python shell
    newReview.save()
    return redirect('/book/')
