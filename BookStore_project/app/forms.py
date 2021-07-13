from django import forms
from django.forms import ModelForm, CharField
from django.forms.fields import MultipleChoiceField
from .models import Book, GENRE_CHOICES, LANGUAGE_CHOICES

class BookForm(forms.ModelForm):
	book_name = CharField(required=True, label="Enter Book Name")
	author_name = CharField(required=True, label="Enter Author Name")

	class Meta:
		model = Book
		fields = ("book_name", "author_name", "genre", "language")
		labels = {"book_name": "Enter Book Name", "author_name": "Enter Author Name", 
				  "genre": "Choose Genre","language": "Choose Language"}

class FilterBooksForm(forms.Form):
	genre = MultipleChoiceField(choices=GENRE_CHOICES)
	language = MultipleChoiceField(choices=LANGUAGE_CHOICES)

	class Meta:
		model = Book
		fields = ("genre", "language")
		labels = {"genre": "Choose Genre","language": "Choose Language"}

