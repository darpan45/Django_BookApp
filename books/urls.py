from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/',views.book_details,name='book_details'),
    path('<int:id>/review/',views.review,name='review'),
]