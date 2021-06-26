from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #render function searches for templates folder in the app
    context={'name':'Darpan'}
    return render(request,'books/index.html',context)