from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='index'),
    #path('<int:pk>/',views.BookDetailView.as_view(),name='book_details'),
    path('<int:id>/',views.book_details,name='book_details'),
    path('<int:id>/review/',views.review,name='review'),
]