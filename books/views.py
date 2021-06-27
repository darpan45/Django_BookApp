from django.http.response import Http404
from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
from .models import Author, Book,Review
from django.views.generic import ListView,DetailView
#booksData=open(r'C:\Users\Darpan\Desktop\Projects\Django 2021\Django-Course\bookstore-Project\books.json').read()

#data=json.loads(booksData)



class BookListView(ListView):
    template_name='books/index.html'
    context_object_name='books'

    def get_queryset(self):
        return Book.objects.all()

# class BookDetailView(DetailView):
#     model=Book
#     template_name="books/book_details.html"
#     # reviews=Review.objects.filter(book_id=id).order_by('-created_at')

#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         context['reviews']=context['book'].review_set.order_by('-created_at')
#         return context

# def index(request):
#     #render function searches for templates folder in the app
#     dbdata=Book.objects.all()
#     context={'books':dbdata}
#     return render(request,'books/index.html',context)

def book_details(request,id):
    try:
        singleBook=Book.objects.get(pk=id)
        #adding minus sign will make reviews in descending order
        reviews=Review.objects.filter(book=id).order_by('-created_at')
        authors=Author.objects.filter(book=id).all()
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    context={'book':singleBook,'reviews':reviews,'authors':authors}
    return render(request,'books/book_details.html',context)

def review(request,id):
    #since form is sending post request,need to handle post request
    body = request.POST.get('review', False)
    newReview=Review(body=body,book_id=id) #entering values in db just like python shell
    newReview.save()
    return redirect('/book/')

def author(request,author_name):
    books=Book.objects.filter(authors__name=author_name)
    context={'books':books}
    return render(request,'books/index.html',context)
