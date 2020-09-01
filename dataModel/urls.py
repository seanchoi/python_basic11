from django.urls import path
from . import views

ulrpatterns = [
    paht('book', views.addBook),
    path('author', views.addAuthor),
    path('book/<int:Book_add.id>', views.bookDetail),
    path('author/<int:Author_add.id>', views.authorDetail)

]