from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm, FilterBooksForm

# Create your views here.
def home(request):
	context = {}
	return render(request, "app/index.html", context)
 
def displayBooks(request):
	books = Book.objects.order_by('-id')[:]
	
	context = {"books": books}
	return render(request, "app/display_books.html", context)

def addBook(request):
	form = BookForm()

	if request.method == "POST":
		form = BookForm(request.POST)
		if form.is_valid():
			form.save()
		
		return redirect("/display-books")

	context = {"form": form}
	return render(request, "app/add_book.html", context)

def filterBooks(request):
	form = FilterBooksForm()

	if request.method == "POST":
		form = FilterBooksForm(request.POST)

		if form.is_valid():
			genre = request.POST.getlist("genre")
			language = request.POST.getlist("language")
			
			books = Book.objects.filter(genre__in=genre, language__in=language)
			
			context = {"books": books}
			return render(request, "app/display_books.html", context)
	
	context = {"form": form}
	return render(request, "app/filter_books.html", context)