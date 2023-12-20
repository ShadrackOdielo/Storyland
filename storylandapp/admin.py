# storylandapp/admin.py
from django.contrib import admin
from .models import Book, UserProfile, Shelf, UserBook

admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(Shelf)
admin.site.register(UserBook)
