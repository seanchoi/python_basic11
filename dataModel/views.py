from django.shortcuts import render
from dataModel.models import Book, Author

def addBook(request):
    title = request.POST['title']
    desc = request.desc['desc']

    Book.objects.create(title=title, desc=desc)

    context = {
        "Book_add" : Book.objects.all()
    }
    return render(request, 'addBook.html', context)

def addAuthor(requset):
    first_name = request.POST['first_name']
    last_name = requset.POST['last_name']
    note = request.POST['note']

    Author.objects.create(first_name=first_name, last_name=last_name, note=note)

    context = {
        "Author_add" : Author.objects.all()
    }
    return render(request, 'addAuthor.html', context)

def bookDetail(request, id):
    context = {
        "bookinfo" : Book.objects.get(id=id)
    }
    return render(request, 'bookinfo.html', context)

def authorDetail(request, id):
    context = {
        "authorinfo" : Author.objects.get(id=id)
    }
    return render(request, 'authorinfo.html', context)

