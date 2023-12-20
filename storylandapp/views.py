# storylandapp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Book, Shelf, UserProfile


def home_view(request):
    return render(request, 'storylandapp/home.html')


@login_required
def user_dashboard(request):
    # Implement user dashboard logic here
    return render(request, 'storylandapp/user_dashboard.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'storylandapp/book_detail.html', {'book': book})


def user_profile(request, username):
    user_profile = get_object_or_404(UserProfile, user__username=username)
    return render(request, 'storylandapp/user_profile.html', {'user_profile': user_profile})


def bookshelf(request, username, shelf_name):
    user = get_object_or_404(UserProfile, user__username=username)
    shelf = get_object_or_404(Shelf, user=user.user, name=shelf_name)
    return render(request, 'storylandapp/bookshelf.html', {'shelf': shelf})
