# storylandapp/models.py
from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True,blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    cover_image_url = models.URLField(blank=True, null=True)
    added_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Shelf(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, related_name='shelves')

    def __str__(self):
        return f"{self.user.username}'s {self.name} Shelf"


class BookStatus(models.TextChoices):
    WANT_TO_READ = 'want_to_read', 'Want to Read'
    READING = 'reading', 'Reading'
    READ = 'read', 'Read'


class UserBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=BookStatus.choices, default=BookStatus.WANT_TO_READ)
    rating = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s {self.status} - {self.book.title}"
