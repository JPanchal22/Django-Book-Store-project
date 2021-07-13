from django.db import models

# Create your models here.
GENRE_CHOICES = (
	("Action and Adventure", "Action and Adventure"), 
	("Classics", "Classics"), 
	("Fiction", "Fiction"), 
	("Sci-Fi", "Sci-Fi"), 
	("Horror", "Horror"), 
	("Personal Development", "Personal Development"), 
	("Comedy", "Comedy"), 
	("Thriller", "Thriller"), 
	("Romance", "Romance"), 
	("Mystery", "Mystery"), 
)

LANGUAGE_CHOICES = (
	("English", "English"),
	("Hindi", "Hindi"),
	("Hungarian", "Hungarian"),
	("Gujarati", "Gujarati"),
	("Marathi", "Marathi"),
	("Spanish", "Spanish"),
	("Italian", "Italian"),
	("French", "French"),
	("Swedish", "Swedish"),
	("Tamil", "Tamil"),
	("Telugu", "Telugu"),
)

class Book(models.Model):
	book_name = models.CharField(max_length=200, blank=True, null=True)
	author_name = models.CharField(max_length=200, blank=True, null=True)
	genre = models.CharField(max_length=50, choices=GENRE_CHOICES, blank=True, null=True)
	language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, blank=True, null=True)

	def __str__(self):
		return self.book_name + " - " + self.author_name

