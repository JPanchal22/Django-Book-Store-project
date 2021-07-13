from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="home"),
	path("display-books/", views.displayBooks, name="display_books"), 
	path("add-book/", views.addBook, name="add_book"),
	path("filter-books/", views.filterBooks, name="filter_books"),
] 