from django.shortcuts import render,redirect
from app1.models import Book
from django.contrib.messages import success
def showIndex(request):
    return render(request,"Index.html")
def save_books(request):
    book_name = request.POST.get("b1")
    author = request.POST.get("b2")
    genre = request.POST.get("b3")
    language = request.POST.get("b4")
    Book(book_name=book_name, author=author, genre=genre, language=language).save()
    success(request, "Book is saved")
    return redirect('showbooklist')
def showbooklist(request):
    book=Book.objects.all()
    return render(request, "showbooklist.html", {"book":book})
def lang(request,data=None):
    if data==None:
        lang=Book.objects.all()
    elif data=="English" or data=="Hindi" or data=="French" or data=="German":
        lang= Book.objects.filter(language=data)
    return render(request, 'showlang.html', {"lang": lang})
def genre(request,data=None):
    if data==None:
        genre=Book.objects.all()
    elif data=="History" or data=="Art" or data=="Mystery" or data=="Economics":
        genre= Book.objects.filter(genre=data)
    return render(request, 'showgenre.html', {"genre": genre})


# Create your views here.
