
# Register your models here.
from django.contrib import admin
from .models import Book, Author

admin.site.register(Book)
admin.site.register(Author)