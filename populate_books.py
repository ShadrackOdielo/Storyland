# populate_books.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storyland.settings')
django.setup()

import requests
from django.contrib.auth.models import User
from storylandapp.models import Book
from django.utils.dateparse import parse_date

# Set up Django environment


def populate_books():
    # Example: Fetch the latest books from the Open Library API
    url = 'https://openlibrary.org/subjects/latest.json?limit=10'
    response = requests.get(url)
    data = response.json()

    # Check if the user exists or create one (adjust as needed)
    user, _ = User.objects.get_or_create(username='example_user')

    # Extract relevant book information and save to the database
    for doc in data['works']:
        title = doc['title']
        author = doc['author_name'][0] if 'author_name' in doc else 'Unknown'
        published_date_str = doc.get('first_publish_year', None)
        published_date = parse_date(published_date_str) if published_date_str and isinstance(published_date_str,
                                                                                             str) else None

        # Create the book using the user
        Book.objects.create(title=title, author=author, published_date=published_date, added_by=user)

if __name__ == '__main__':
    populate_books()
